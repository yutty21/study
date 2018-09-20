
import urllib.request

print("正在下载数据....")
url = "http://www.neihan8.com/article/list_5_1.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)

# 获取每页的HTML源码字符串
html = response.read()


print(str(html))

