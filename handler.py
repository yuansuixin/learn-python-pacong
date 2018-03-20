# -*- coding:UTF-8 -*-
import urllib.request

handler = urllib.request.HTTPHandler()

opener = urllib.request.build_opener(handler)

url  = 'https://www.baidu.com/'
request = urllib.request.Request(url)
response = opener.open(request)

print(response.read().decode())