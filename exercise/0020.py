#-*- coding: utf-8 -*-
__author__ = "coolfire"
import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password,salt=None):
	"""Hash password on the fly."""
	if salt is None:
		salt = os.urandom(8) #64 bits

	assert 8 == len(salt)
	assert isinstance(salt,str)

	if isinstance(password,unicode):
		password = password.encode('UTF-8')

	assert isinstance(password,str)

	result = password
	for i in xrange(10):
		result = HMAC(result,salt,sha256).digest()
	return salt + result

hashed = encrypt_password("12345678")
def validate_password(hashed,input_password):
	return hashed == encrypt_password(input_password,salt=hashed[:8])
assert validate_password(hashed,'12345678')