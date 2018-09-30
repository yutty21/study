# urllib2_get.py
import urllib.request
import urllib.parse
import re
import json

#url = "http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=100"
url = "http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=1000&issueStart=&issueEnd=&dayStart=2012-10-24&dayEnd=2018-09-27&pageNo="
#word = {"wd":"name=ssq&issueCount=30"}
#word = urllib.parse.urlencode(word) #转换成url编码格式（字符串）
#newurl = url + "?" + word    # url首个分隔符就是 ?

#headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
headers = {"Referer":"http://www.cwl.gov.cn/kjxx/ssq/kjgg/"}




request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

str1 = response.read().decode()

jsonObj = json.loads(str1)

result = jsonObj["result"]
for item in result :
    print(item["date"] + ", red = "  + item["red"] + "  ,blue = "+item["blue"])
    pass
