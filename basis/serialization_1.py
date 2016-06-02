#-*- coding: utf-8 -*-
__author__ = "coolfire"
import cPickle
f = open("info.pkl","r+")
info2_dict = cPickle.load(f)
info2_dict['age'] = 110
cPickle.dump(info2_dict,f)
f.close()
exit()