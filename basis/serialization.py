#-*- coding: utf-8 -*-
__author__ = "coolfire"
import cPickle
info_dict = {'name':'yeho','age':100,'Lang':'Python'}
f = open('info.pkl','wb')
cPickle.dump(info_dict,f)
f.close()
#exit()

obj = 123,"abcdedf",["ac",123],{"key":"value","key1":"value1"}
test_data = cPickle.dumps(obj)


test1_data = cPickle.loads(test_data)
print type(test1_data)