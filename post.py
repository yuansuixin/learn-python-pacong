# -*- coding:UTF-8 -*-
import json
import urllib.request
import urllib.parse


post_url = 'http://fanyi.youdao.com/'
word = 'baby'
data = {
    'kw':word,
}
# 处理数据,现将数据拼接起来，然后需要进行编码成字节类型
data= urllib.parse.urlencode(data).encode()

headers = {
    'User-Agen': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

request = urllib.request.Request(post_url,headers=headers)
response = urllib.request.urlopen(request,data=data)
# print(response.read().decode())
# json格式的字符串
obj = response.read().decode()
# 将json格式的字符串转化为对象
obj = json.loads(obj)
# 以只写的方式打开文件
fp = open('baidu.txt','w',encoding='utf-8')
# 将json对象直接写入到文件中
json.dump(obj,fp,ensure_ascii=False)
fp.close()












