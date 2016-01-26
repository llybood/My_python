# -*- coding: utf-8 -*-
__author__ = "coolfire"
filter = open("filtered_words.txt","r",)

input_word = raw_input("please input the words:")

words_list = []
for f in filter.readlines():
    words_list.append(f.strip('\r\n'))

if input_word in words_list:
    print "Freedom"
else:
    print "Human Rights"