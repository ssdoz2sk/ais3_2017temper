import requests
import base64
import time

token = "MS01Y2QwMjNhN2E4NjJiYWZiODYwYTljMTk1YzMwMzRiNzljOWNjNzIw"
while True:
	r = requests.get('http://10.13.2.43:31532/', headers={"Token": token})
	token = r.headers.get('Next-Token')
	print "{} - {}".format(r.text.strip(), token)
	print base64.b64decode(token)
#	time.sleep(1)
