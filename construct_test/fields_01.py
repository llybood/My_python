#-*- coding: utf-8 -*-
__author__ = "coolfire"
from construct import Adapter,Bytes,Construct,Struct
from construct import UBInt16,ULInt16,Byte

UBInt16("foo").parse("\x01\x02")
ULInt16("foo").parse("\x01\x02")

class IpAddressAdapter(Adapter):
	def _encode(self,obj,context):
		return "".join(chr(int(b)) for b in obj.split())
	def _decode(self,obj,context):
		return ".".join(str(ord(b)) for b in obj)

#IpAddressAdapter(Bytes("foo",4)).parse("\x01\x02\x03\x04")



class PrintContext(Construct):
	def _parse(self, stream, context):
		print context
		print "hello"

foo = Struct("foo",
			 Byte("a"),
			 Byte("b"),
			 PrintContext("c"),
			 Struct("bar",
					Byte("a"),
					Byte("b"),
					PrintContext("c"),
					),
			 PrintContext("d"),
			 )

foo.parse("\x01\x02\x03\x04")


