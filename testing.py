#!/usr/bin/env python3

# 将汉字转码并生成URL, 在浏览器中打开
import webbrowser
import sys

# testing git command.

def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

s = input()

print (s.encode('gb2312'))

ans = is_contains_chinese(s)

if ans == True:
    qurl = 'https://s.1688.com/selloffer/offer_search.htm?keywords=' + str(s.encode('gb2312')).replace('\\x', '%')[2:-1]
else:
    qurl = 'https://s.1688.com/selloffer/offer_search.htm?keywords=' + str(s.encode('gb2312')).replace('\\x', '%')


# n=s.encode('gbk')
# m=str(s.encode('gb2312'))
# print(n)

webbrowser.open(qurl)




# mn = m.decode("utf-8")
# print (mn)
# mm = m.decode("utf-8")
# type (mm)
# print (mm)


# website_bytes_gb2312.decode("gb2312")

# str(s, encoding = "utf-8")

#
# print(str(m).replace('\x','%'))

# s = '我是一串汉字''
# s.decode('utf-8').encode('gbk')
#
# print(s)

# # 判断URL编码方式
# import requests
#
# url = 'https://s.1688.com/selloffer/offer_search.htm?keywords=%C0%AF%D6%F2&button_click=top&n=y&netType=1%2C11'
# # print (requests.get(url).encoding)
# r = requests.get(url)
# r.encoding = 'GBK'
# print (r.text)

# r = 'https://s.1688.com/selloffer/offer_search.htm?keywords=%C0%AF%D6%F2&button_click=top&n=y&netType=1%2C11'
# r.encoding = 'GBK'
# print(r)