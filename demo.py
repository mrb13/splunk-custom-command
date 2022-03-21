import requests
import sys
import json
sys.path.append('/opt/splunk/lib/python3.7')
sys.path.append('/opt/splunk/lib/python3.7/site-packages/splunk')
sys.path.append('/opt/splunk/lib/python2.7')
sys.path.append('/opt/splunk/lib/python2.7/site-packages/splunk')

import Intersplunk as man

response =requests.get("https://randomuser.me/api/")


dataa = json.loads(response.text)
#print(dataa["results"][0]["name"])
result = []
result.append(dataa["results"][0]["name"])

man.outputResults(result)



 