#-*- coding: utf-8 -*-
__author__ = 'coolfire'

'''
def myfunc():
    print("myfunc() called.")

myfunc()
myfunc()
'''
'''
def deco(func):
    print "before myfunc() called."
    func()
    print "after myfunc() called."
    return func

def myfunc():
    print "myfunc() called."

myfunc = deco(myfunc)
myfunc()
myfunc()
'''
'''
import time

def foo():
    print "in foo()"

def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print 'used:', end-start

    return wrapper

foo = timeit(foo)
foo()
'''

def test1():
    def test2():
        x = 1
        y = 2
        print x + y
    return test2

test3 = test1
test3() 

