#!/usr/bin/python
# encoding:utf-8
# -*- Mode: Python -*-
# Author: Soros Liu <soros.liu1029@gmail.com>

# ==================================================================================================
# Copyright 2016 by Soros Liu
#
#                                                                          All Rights Reserved
"""
Split the big image into two small image according to the odd/even index
"""
from PIL import Image
__author__ = 'Soros Liu'
org_img = Image.open('cave.jpg', 'r')
width, height = org_img.size
imgs = [Image.new(org_img.mode, (width // 2, height // 2)) for dummy_i in range(2)]
imgs_load = [image.load() for image in imgs]
org_load = org_img.load()

for i in range(width):
    for j in range(height):
        org_pos = (i, j)
        if (i % 2 == 0 and j % 2 == 0) or \
                (i % 2 == 1 and j % 2 == 1):
            dst_pos = (i // 2, j // 2)
            imgs_load[i % 2][dst_pos] = org_load[org_pos]

[imgs[i].save('cave%d.png' % i) for i in range(2)]



