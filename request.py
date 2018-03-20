# -*- coding:UTF-8 -*-
import urllib
import ssl

# 解决证书的问题
ssl._create_default_https_context=ssl._create_stdlib_context

url = 'http://www.baidu.com/'
response = urllib.request.urlopen(url)
# 自己定制头部，通过url和头部构建请求对象
headers = {
    'User-Agen':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}


request = urllib.request.Request(url,headers=headers)

#  发送请求对象

print(response.read().decode())