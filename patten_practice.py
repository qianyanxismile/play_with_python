#coding=utf-8

import re


m = re.search(r"(121){2}","12345678")
print m 

m = re.search(r"(121){2}", "121121")
print m.group() #返回匹配的字符串
print m.group(1)#返回第一个组内容
print m.groups()#返回所有组内容

p = r"(?P<quhao>\d{3,4})-(?P<phone>\d{7,8})"

m = re.search(p,"029-6663123")

print m.group("quhao")
print m.group("phone")
print m.groups()
print m.group(1)#或通过名称匹配 

"""场景：匹配要保证开始与结束保持一致，采用反向引用'\group_id'"""
#p = r"<([\w]+)>.*<([\w]+)>"
p = r"<([\w]+)>.*<\1>"

m = re.search(p, "<a>asd123asd<a>")
print m

m = re.search(p, "<a>asd123asd<b>")
print m

p = r"\w+(\.jpg|\.png|\.bmp)"

s = "img1.jpg,img2.png,img3.bmp"

m = re.findall(p,s)

print  m

p = r"\w+(?:\.jpg|\.png|\.bmp)"

m = re.findall(p,s)

print  m

regular_v2 = re.findall(r"^https","https://docs.python.org/3/whatsnew/3.6.html")
print regular_v2

text = "i like python and Python"
p = r"[pP]ython"
match_iter = re.finditer(p,text)
#m = match_iter.group()
for i in match_iter:
	print i.group()

test = "asd123zxc456qwe"
p = r"\d+"
m = re.sub(p,"replace",test)
print m
m = re.sub(p,"",test,count=1)
print m
m = re.sub(p,"",test,count=2)
print m


text = "我喜欢学习哈哈哈哈python"
p = r"\w+"
regex = re.compile(p, re.U)
m = regex.search(text)
print m.end()
