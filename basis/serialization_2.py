#-*- coding: utf-8 -*-
__author__ = "coolfire"
import cPickle
#Python标准库提供pickle和cPickle模块。cPickle是用C编码的，
#在运行效率上比pickle要高，但是cPickle模块中定义的类型不能被继承
#（其实大多数时候，我们不需要从这些类型中继承，推荐使用cPickle）。
# cPickle和pickle的序列化/反序列化规则是一样的，使用pickle序列化一个对象，
# 可以使用cPickle来反序列化。同时，这两个模块在处理自引用类型时会变得更加“聪明”，
# 它不会无限制的递归序列化自引用对象，对于同一对象的多次引用，它只会序列化一次。
f = open('info.pkl','r+')
info_dict = cPickle.load(f)
print info_dict

info2_dict = cPickle.load(f)
print info2_dict

info3_dict = cPickle.load(f)
print info3_dict

