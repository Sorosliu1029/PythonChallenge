#!/usr/bin/python
# encoding:utf-8
# -*- Mode: Python -*-
# Author: Soros Liu <soros.liu1029@gmail.com>

# ==================================================================================================
# Copyright 2016 by Soros Liu
#
#                                                                          All Rights Reserved
"""
Refer to online solution: http://blog.csdn.net/kosl90/article/details/7270605
"""
__author__ = 'Soros Liu'
with open('evil2.gfx', 'rb') as f:
    img = f.read()
for dummy_i in range(5):
    with open('pic_%d.jpg' % dummy_i, 'wb') as f:
        f.write(img[dummy_i::5])

