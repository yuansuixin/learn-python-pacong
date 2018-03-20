import urllib.request
import urllib.parse

# 通过抓包分析，哪个是post url
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
# 抓包分析，post请求需要的参数
data = {
	'cname': '乌镇',
	'pid': '',
	'pageIndex': '1',
	'pageSize': '10',
}
# 对post数据进行处理
data = urllib.parse.urlencode(data).encode()
# 自己加的头部，如果没有数据，头部信息全部拿过来，有两个不需要，一个accept-encoding  content-length
headers = {
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
}
# 构建请求对象，发送请求
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request, data=data)

print(response.read().decode())