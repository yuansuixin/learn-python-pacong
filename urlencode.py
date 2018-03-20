# -*- coding:UTF-8 -*-

# url = 'http://www.baidu.com/index.html?username=goudan&password=1234&age=88&height=188'
import urllib.parse

url = 'http://www.baidu.com/index.html?'
username = '狗蛋'
age = 18
height = 188
password = '34567'
weight = 177

data = {
    'username':username,
    'age':age,
    'height':height,
    'password':password,
    'weight':weight,
}
# 自己实现
# query = ''
# for k,v in data.items():
#     query  = query+'&'+ k +'='+str(v)
# query = query.lstrip('&')
# url = url+query
# url = urllib.parse.quote(url)
# print(query)

query = urllib.parse.urlencode(data)
url += query
print(url)


