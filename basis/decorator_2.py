#-*- coding: utf-8 -*-
__author__ = 'coolfire'

def getTalk(type='shout'):

    def shout(word='yes'):
        return word.capitalize()+"!"

    def whisper(word='yes'):
        return word.lower()+"..."

    if type == 'shout':
        return shout
    else:
        return whisper


talk = getTalk()
print talk()

