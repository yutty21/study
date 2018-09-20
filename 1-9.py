import re
import urllib.request

url = "http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=30"
headers = {"Referer":"http://www.cwl.gov.cn/kjxx/ssq/kjgg/"}

request = urllib.request.Request(url,headers=headers )
response = urllib.request.urlopen(request)
string = response.read().decode()

patt ='.+\d+-\d+-\d+'

str1 = re.search(patt,string).group()
str2 = re.match(patt,string)
print(str1)
print(str2)
print(string)