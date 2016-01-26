#-*- coding: utf-8 -*-
# 统计一个纯英文文本文件里面单词的个数


#打开一个文件
f = open("C:\Users\coolfire\Documents\\test.txt","r")
c = 0
for lines in f:
    words = lines.split()
    c += len(words)
print c
