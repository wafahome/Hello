# !/usr/bin/python
# encoding: utf-8

# # 将汉字转码并生成URL, 在浏览器中打开
# import sys
#
# # Workflow3 supports Alfred 3's new features. The `Workflow` class
# # is also compatible with Alfred 2.
# from workflow import Workflow3


import webbrowser

s = '中华人民共和国'  # %C0%AF%D6%F2
n=s.encode('gbk')
m=str(s.encode('gb2312'))
print(n)
# qurl = 'https://s.1688.com/selloffer/offer_search.htm?keywords=' + str(s.encode('gb2312')).replace('\\x','%')[2:-1]
# webbrowser.open(qurl)
