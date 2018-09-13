# urllib2_get.py
import urllib.request
import urllib.parse
import re

url = "http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=30"
#word = {"wd":"name=ssq&issueCount=30"}
#word = urllib.parse.urlencode(word) #转换成url编码格式（字符串）
#newurl = url + "?" + word    # url首个分隔符就是 ?

#headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
headers = {"Referer":"http://www.cwl.gov.cn/kjxx/ssq/kjgg/"}



request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

str1 = response.read().decode()

str2 = re.split('red',str1)
str3 = re.split(',|(?=(?:\d{5}|[A-Z]{2}))',str1)

str4 = re.match('red',str1)
if str4 is not None:
    print(str4)

print(str1)
print(str2)
print(str3)
print(str4)
