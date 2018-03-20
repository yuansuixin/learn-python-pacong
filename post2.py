# -*- coding:UTF-8 -*-
import urllib

post_url = ''
data = {
    'form':'en',
'to':'zh',
'query':'dog',
'transtype':'realtime',
'simple_means_flag':'3',
'sign':'',
'token':'',
}

heads={

}

request = urllib.request.Request(post_url,headers=heads)





