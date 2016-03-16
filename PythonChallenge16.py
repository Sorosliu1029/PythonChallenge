#!/usr/bin/python
# encoding:utf-8
# -*- Mode: Python -*-
# Author: Soros Liu <soros.liu1029@gmail.com>

# ==================================================================================================
# Copyright 2016 by Soros Liu
#
#                                                                          All Rights Reserved
"""
align the pink bar to the left
"""
from PIL import Image
__author__ = 'Soros Liu'
img = Image.open('mozart.gif', 'r')

img = img.convert('RGB')
for y in range(img.size[1]):
    row_color = [img.getpixel((x, y)) for x in range(img.size[0])]
    idx = row_color.index((255, 0, 255))
    row_color = row_color[idx:] + row_color[:idx]
    [img.putpixel((x, y), value) for x, value in enumerate(row_color)]
img.show()
