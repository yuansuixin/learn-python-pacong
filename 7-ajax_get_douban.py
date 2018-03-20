import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
# sql语句中有个limit
# select * from user limit 5,5
# 9条数据，每页显示3条
# offset,number
# 第一页sql语句：select * from user limit 0,3
# 第二页：select * from user limit 3,3
# 第三页：select * from user limit 6,3
# 第n页   limit (n-1)*3,3
page = int(input('请输入想要的页码:'))
limit = 20
start = (page - 1) * limit

# 写个字典，包含这两个参数
data = {
	'start': start,
	'limit': limit
}
# 根据生成的query字符串拼接指定的url
query = urllib.parse.urlencode(data)
url += query

# print(url)
# 构建请求对象，发送请求
headers = {
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
}
request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

# print(response.read().decode())
with open('douban.txt', 'wb') as fp:
	fp.write(response.read())