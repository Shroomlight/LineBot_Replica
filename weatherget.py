import urllib.request as request
import json as js
nhtech="https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-850C0B7B-8172-4E44-AE39-5023FC83C899&locationName=%E5%B1%8F%E6%9D%B1%E7%B8%A3"
with request.urlopen(nhtech) as response:
    data=js.load(response)
weather=data["records"]["location"]
print (weather)
# clist=nhtech["result"]["results"]
# for company in clist:
#     print(company["公司名稱"])