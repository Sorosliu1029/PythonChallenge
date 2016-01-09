#!/usr/bin/python
# encoding:utf-8
# -*- Mode: Python -*-
# Author: Soros Liu <soros.liu1029@gmail.com>

# ==================================================================================================
# Copyright 2016 by Soros Liu
#
#                                                                          All Rights Reserved
"""
use bz2 library is the key to solving the challenge
i tried to convert the string to raw string(like r'balabala') or to the byte(like b'balabala', but sadly failed
i will thanks a lot if anyone could tell me how to do the above stuff :) ☺️
the last thing is just decompressing the bz string and you will get the solution
"""
import bz2
import re
from urllib import request
__author__ = 'Soros Liu'
with request.urlopen('http://www.pythonchallenge.com/pc/def/integrity.html') as f:
    source = f.read().decode('utf-8')
    compressed_un = re.findall(r'un:\s+\'(.*?)\'', source)[0]
    compressed_pw = re.findall(r'pw:\s+\'(.*?)\'', source)[0]
    print(compressed_un + '\n' + compressed_pw)
    un = bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084').decode('utf-8')
    pw = bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08').decode('utf-8')
    print(un + '\n' + pw)

