#-*- coding: utf-8 -*-
__author__ = "coolfire"

def container(start,end):
	while start <= end:
		yield start
		start += 1

c = container(0,5)
print type(c)
print next(c)
next(c)

for i in c:
	print(i)