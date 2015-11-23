#-*- coding: utf-8 -*-
__author__ = "coolfire"

import string

input_words = raw_input("Please enter your words: ")

filter_words = open("filtered_words.txt","r")



for f in filter_words.readlines():
    word = f.strip("\r\n")
    input_words = input_words.replace(word,"**")

print input_words
