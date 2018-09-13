
from urllib import request
from urllib import parse
from urllib.request import urlopen

#values = {'username': '782265537', 'password': 'yqc123456789,.'}
#data = parse.urlencode(values).encode('utf-8')  # 提交类型不能为str，需要为byte类型
url = 'https://blog.csdn.net/'
request = request.Request(url)
response = urlopen(request)
print(response.read().decode())