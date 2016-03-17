#!/usr/bin/python
# encoding:utf-8
# -*- Mode: Python -*-
# Author: Soros Liu <soros.liu1029@gmail.com>

# ==================================================================================================
# Copyright 2016 by Soros Liu
#
#                                                                          All Rights Reserved
"""

"""
from http import cookiejar
from urllib import request
import re
__author__ = 'Soros Liu'

cj = cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
r = opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345')
cookie = cj.make_cookies(r, opener)
print(cookie)
r = opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=44827')
cookie = cj.make_cookies(r, opener)
print(cookie)