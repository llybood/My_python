#-*- coding: utf-8 -*-
__author__ = "coolfire"
class Container:
    def __init__(self,start=0,end=0):
        self.start = start
        self.end = end
    def __iter__(self):
        print "[LOG] I made this iterator!"
        return self

    def next(self):
        print "[LOG] I made this iterator!"
        if self.start <= self.end:
            i = self.start
            self.start += 1
            return i
        else:
            raise StopIteration

c = Container(0,5)
for i in c:
	print i