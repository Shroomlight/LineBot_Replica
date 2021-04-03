import json as js

import codecs

import os

# weatherFlex=js.load(codecs.open("weather.json","r+","utf-8-sig"))
# imgUrl_1=weatherFlex["contents"][0]["hero"]["url"]
# city_1=weatherFlex["contents"][0]["body"]["contents"][0]["text"]
# weather_1=weatherFlex["contents"][0]["body"]["contents"][1]["text"]
# iconh_1=weatherFlex["contents"][0]["body"]["contents"][2]["contents"][0]["contents"][0]["url"]
# temp_1=weatherFlex["contents"][0]["body"]["contents"][2]["contents"][0]["contents"][1]["text"]
# tempest_1=weatherFlex["contents"][0]["body"]["contents"][2]["contents"][0]["contents"][2]["text"]
# iconw_1=weatherFlex["contents"][0]["body"]["contents"][2]["contents"][1]["contents"][0]["url"]
# rain_1=weatherFlex["contents"][0]["body"]["contents"][2]["contents"][1]["contents"][1]["text"]
# rainpr_1=weatherFlex["contents"][0]["body"]["contents"][2]["contents"][1]["contents"][2]["text"]
# comfor_1=weatherFlex["contents"][0]["body"]["contents"][3]["contents"][0]["text"]
# times_1=weatherFlex["contents"][0]["body"]["contents"][4]["text"]
# butcolor_1=weatherFlex["contents"][0]["footer"]["contents"][0]["color"]

# city={"text":"屏東縣"}
# with open("./replica/weather.json",mode="r+",encoding="utf-8") as weatherdata:
#     data=weatherdata.read()
#     js.dump(city, data["contents"][0]["body"]["contents"][0]["text"],indent = 6)
    
#     print(data)

#完成json檔案Value修改
w=js.load(codecs.open("./replica/test.json","r+","utf-8-sig"))
w["contents"][0]["body"]["contents"][0]["text"]="屏東縣"
j = js.dumps(w,ensure_ascii=False)
os.remove("./replica/test.json")
f=open("./replica/test.json",mode="w",encoding="utf-8")
f.write(str(j))
print(j)
f.close()



    


# import urllib.request as urlrequest

# cwbdata="https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-850C0B7B-8172-4E44-AE39-5023FC83C899&locationName=%E5%B1%8F%E6%9D%B1%E7%B8%A3"
# with urlrequest.urlopen(cwbdata) as response:
#     data=js.load(response)
# startTime=(data["records"]["location"][0]['weatherElement'][0]['time'][0]['startTime'])
# endTime=(data["records"]["location"][0]['weatherElement'][0]['time'][0]['endTime'])

# y=[]
# for value in range(5):
#     x=data["records"]["location"][0]['weatherElement'][value]['time'][0]['parameter']['parameterName']
#     y.append(x)
#     if value == 4:
#         print(y)

# f_wx="天氣現象："+y[0]
# f_pop="降雨機率："+y[1]+"%"
# f_ci="舒適度："+y[3]
# f_maxT="最高溫度："+y[4]
# f_minT="最低溫度："+y[2]

# print(startTime+"\n"+endTime)
# print(f_wx+"\n"+f_pop+"\n"+f_ci+"\n"+f_maxT+"\n"+f_minT)

# print()