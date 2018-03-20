# -*- coding:UTF-8 -*-
import urllib

url = 'https://www.baidu.com/index.html?username=马云'
# url编码和解码,将url中的非法字符中文进行编码
string = urllib.parse.quote(url)
string = urllib.parse.unquote(string)
print(string)







