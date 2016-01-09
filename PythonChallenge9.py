#!/usr/bin/python
# encoding:utf-8
# -*- Mode: Python -*-
# Author: Soros Liu <soros.liu1029@gmail.com>

# ==================================================================================================
# Copyright 2016 by Soros Liu
#
#                                                                          All Rights Reserved
"""
still PIL library
get the first and second line data and connect dots together
"""
import re
from PIL import ImageDraw, Image
__author__ = 'Soros Liu'
with open('return_good.html') as f:
    source = f.read()
source = ''.join(source.split('\n'))
content = re.findall(r'(<!\-\-.*?\-\->)', source)[1]
first = list(map(int, re.findall(r'first:(.*)second', content)[0].split(',')))
second = list(map(int, re.findall(r'second:(.*)-->', content)[0].split(',')))
img = Image.open('good.jpg')
new_img = Image.new(img.mode, img.size)
draw = ImageDraw.Draw(new_img)
draw.line(first)
draw.line(second)
new_img.show(title='result')