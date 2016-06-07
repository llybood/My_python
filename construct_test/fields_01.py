#-*- coding: utf-8 -*-
__author__ = "coolfire"
from construct import UBInt16,ULInt16
UBInt16("foo").parse("\x01\x02")
ULInt16("foo").parse("\x01\x02")