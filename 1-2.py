# urllib2_urlopen.py

# 导入urllib2 库
import urllib.request

# 向指定的url发送请求，并返回服务器响应的类文件对象
response = urllib.request.urlopen("http://www.baidu.com")

# 类文件对象支持 文件对象的操作方法，如read()方法读取文件全部内容，返回字符串
html = response.read()

# 打印字符串
print(html)