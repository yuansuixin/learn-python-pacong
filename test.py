# -*- coding:UTF-8 -*-
import os
import urllib.request
import urllib.parse

import time

# 该函数功能是根据page生成指定的请求对象
# url：原始的url，在这个基础上进行拼接
# page：当前页码
def handler_request(url, page):
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'
    # }
    pn = (page - 1) * 50
    url = url + 'pn=%s' % pn
    # url = urllib.parse.urlencode(url)
    print(url,'----------url')
    request = urllib.request.Request(url)
    print(request)
    return request
# 根据请求对象，发送请求，获取数据，保存数据
def download_files(request, baming, page):
    data={
        'kw':baming
    }
    data = urllib.parse.urlencode(data).encode()
    print(data)
    print('开始下载')
    response = urllib.request.urlopen(request)
    print(response)
    # 创建文件夹,如果不存在，创建一个
    if not os.path.exists(baming):
        os.mkdir(baming)

    # 保存内容到指定的文件夹内
    # 拼接文件名
    filename = '第' + str(page) + '页.html'
    # 获取文件的路径
    filepath = os.path.join(baming, filename)
    # 将数据写入到文件中即可
    with open(filepath, 'wb') as fp:
        fp.write(response.read())


def main():
    # baming = input('请输入吧名：')
    baming = '司机吧'
    # start = int(input('请输入开始的页码：'))
    start = 1
    # end = int(input('请输入结束的页码：'))
    end = 5
    # urlbaming = urllib.parse.urlencode(baming)
    url = 'http://tieba.baidu.com/f?kw=%s&ie=utf-8&' % urllib.parse.quote_plus(baming)

    for page in range(start, end + 1):
        print('----------------')
        print('开始下载第%s页......' % page)
        # 根据页码生成请求对象
        request = handler_request(url, page)
        print('=================')
        print(request)
        # 根据请求对象，发送请求，获取数据、保存数据
        print('结束下载第%s页' % page)
        download_files(request, baming, page)
        time.sleep(3)


if __name__ == '__main__':
    main()
