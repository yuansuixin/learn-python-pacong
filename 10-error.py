import urllib.request
import urllib.parse
import urllib.error

# urlerror
# url = 'http://www.maodan.com/'

# httperror
url = 'http://blog.csdn.net/xuyuqingfeng953/article/details/52794365'


try:
	response = urllib.request.urlopen(url)
	print(response.read())
# 如果两个异常都想写道这里，要先写子类，再写父类
# except urllib.error.URLError as e:
except urllib.error.HTTPError as e:
	print(e)
except urllib.error.URLError as e:
	print(e)
