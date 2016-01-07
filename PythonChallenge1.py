"""
string library function: maketrans and translate
like a kind of encryption and decryption
enjoy python :)
"""
import string
__author__ = 'Soros Liu'

cryptogram = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw
fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq
pcamkkclbcb. lmu ynnjw ml rfc spj.'''
translate_table = cryptogram.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
print(cryptogram.translate(translate_table))
# below is meaningful code
print('map'.translate(translate_table))