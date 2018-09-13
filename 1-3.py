#urllib2_useragent.py

import urllib.request

url = "http://www.itcast.cn"

#IE 9.0 的 User-Agent，包含在 ua_header里
ua_header = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

#  url 连同 headers，一起构造Request请求，这个请求将附带 IE9.0 浏览器的User-Agent
request = urllib.request.Request(url, headers = ua_header)

# 向服务器发送这个请求
response = urllib.request.urlopen(request)

html = response.read()
print(html)