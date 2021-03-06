import urllib.request as request
import json as js

cwbdata="https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-850C0B7B-8172-4E44-AE39-5023FC83C899&locationName=%E5%B1%8F%E6%9D%B1%E7%B8%A3"
with request.urlopen(cwbdata) as response:
    data=js.load(response)
startTime=(data["records"]["location"][0]['weatherElement'][0]['time'][0]['startTime'])
endTime=(data["records"]["location"][0]['weatherElement'][0]['time'][0]['endTime'])

y=[]
for value in range(5):
    x=data["records"]["location"][0]['weatherElement'][value]['time'][0]['parameter']['parameterName']
    y.append(x)
    if value == 4:
        print(y)

f_wx="天氣現象："+y[0]
f_pop="降雨機率："+y[1]+"%"
f_ci="舒適度："+y[3]
f_maxT="最高溫度："+y[4]
f_minT="最低溫度："+y[2]

print(startTime+"\n"+endTime)
print(f_wx+"\n"+f_pop+"\n"+f_ci+"\n"+f_maxT+"\n"+f_minT)

# wx=(data["records"]["location"][0]['weatherElement'][0]['time'][0]['parameter']['parameterName'])
# pop=(data["records"]["location"][0]['weatherElement'][1]['time'][0]['parameter']['parameterName'])
# ci=(data["records"]["location"][0]['weatherElement'][3]['time'][0]['parameter']['parameterName'])
# minT=(data["records"]["location"][0]['weatherElement'][2]['time'][0]['parameter']['parameterName'])
# maxT=(data["records"]["location"][0]['weatherElement'][4]['time'][0]['parameter']['parameterName'])
# print(startTime+"\n"+endTime+"\n"+wx+"\t"+pop+"%"+ci+minT+maxT)

#     print(company["公司名稱"])