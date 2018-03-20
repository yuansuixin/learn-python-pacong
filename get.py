# -*- coding:UTF-8 -*-

import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?ie=UTF-8'

name = '古力娜扎'
data = {
    'wd':name,
}

query = urllib.parse.urlencode(data)
url = url + '&' + query
print(url)

headers = {
    'User-Agen': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)

with open('guli.heml','wb') as fp :
    fp.write(response.read())





