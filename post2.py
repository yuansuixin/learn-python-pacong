
import urllib.request
import urllib.parse

post_url = 'http://fanyi.baidu.com/v2transapi'

word = 'dog'
data = {
	'from': 'en',
	'to': 'zh',
	'query': word,
	'transtype': 'realtime',
	'simple_means_flag': '3',
	'sign': '871501.634748',
	'token': 'eb6762ad9a140deb3d767d6b15eb6e2f',
}

data = urllib.parse.urlencode(data).encode()
headers = {
	'Host': 'fanyi.baidu.com',
	'Connection': 'keep-alive',
	#'Content-Length': '120',
	'Accept': '*/*',
	'Origin': 'http://fanyi.baidu.com',
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Referer': 'http://fanyi.baidu.com/?aldtype=16047',
	#'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Cookie': 'BAIDUID=4C9140721601C42DF10A3CB2579CB852:FG=1; BIDUPSID=4C9140721601C42DF10A3CB2579CB852; PSTM=1521446112; H_PS_PSSID=; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1521513364; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1521513364; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D'
}
request = urllib.request.Request(post_url, headers=headers)
response = urllib.request.urlopen(request, data=data)

print(response.read().decode())



