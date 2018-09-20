

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
import re

from click._compat import raw_input

url = "https://movie.douban.com/chart"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
request = urllib.request.Request(url, headers = headers)
response = urllib.request.urlopen(request)

        # 获取每页的HTML源码字符串
html = response.read()
        #print (html)
print (html)
        # 创建正则表达式规则对象，匹配每页里的段子内容，re.S 表示匹配全部字符串内容
pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>', re.S)

        # 将正则匹配对象应用到html源码字符串里，返回这个页面里的所有段子的列表
content_list = pattern.findall(str(html))

print(content_list)
        # 调用dealPage() 处理段子里的杂七杂八
#self.dealPage(content_list)

#for item in content_list:
    # 将集合里的每个段子按个处理，替换掉无用数据
item = str(html).replace("<p>","").replace("</p>", "").replace("<br>", "")
    #print item.decode("gbk")
    #  处理完后调用writePage() 将每个段子写入文件内
    #self.writePage(item)

print ("正在写入数据....")
with open("duanzi1.txt", "a") as f:
    f.write(item)


