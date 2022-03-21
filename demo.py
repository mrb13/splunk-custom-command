import requests
import sys
import json
sys.path.append('/opt/splunk/lib/python3.7')
sys.path.append('/opt/splunk/lib/python3.7/site-packages/splunk') 
sys.path.append('/opt/splunk/lib/python2.7')
sys.path.append('/opt/splunk/lib/python2.7/site-packages/splunk')

import Intersplunk as man

x1 = sys.argv[1]
xx = int(x1)
#print(x1)
#print(xx)
response =requests.get("https://randomuser.me/api/")
dataa = json.loads(response.text)
#print(dataa["results"][0]["name"])
result = []
result.append(dataa["results"][xx]["name"])

man.outputResults(result)
