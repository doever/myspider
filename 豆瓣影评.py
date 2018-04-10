# -*- coding:utf-8 -*-
import requests
import re
import time
def spider_douban():
    url="https://movie.douban.com/review/best/?start=20"
    res = requests.get(url)
    print(res.status_code)
    res.encoding="UTF-8"
    return res.content
def save_content(text):
    f=open("C:/users/administrator/desktop/douban.txt","wb")
    f.write(text)


a=spider_douban()
print(type(a))
save_content(a)
with open("C:/users/administrator/desktop/douban.txt","r",encoding='UTF-8') as filename:
    douban_text=filename.readlines()
name=re.findall(r'class="name">(.*?)</a>',str(douban_text))
print(name)
# print(name.group(1))
