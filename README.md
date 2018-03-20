# learn-python-pacong
学习Python爬虫阶段的代码练习

# test.py 爬取贴吧

- 代码一直都是可以爬取英文吧名的网页，而中文的就会遇到这个错误，

```
UnicodeEncodeError: 'ascii' codec can't encode characters in..

```
- 我通过将kw进行urlencode（）编码成url格式，就会报另一个错误，如下：

```

TypeError: not a valid non-string sequence or mapping ob 

```

- 将kw中文的参数进行urllib.parse.quote_plus（）进行编码，就可以实现爬取中文吧名的网页


