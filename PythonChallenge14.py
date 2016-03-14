#!/usr/bin/python
# encoding:utf-8
# -*- Mode: Python -*-
# Author: Soros Liu <soros.liu1029@gmail.com>

# ==================================================================================================
# Copyright 2016 by Soros Liu
#
#                                                                          All Rights Reserved
"""
Nothing tricky, just follow the picture pattern and refactor the original image
"""
from PIL import Image
__author__ = 'Soros Liu'
org_img = Image.open('wire.png')
dst_img = Image.new(org_img.mode, (100, 100))


def copy_pixel(org_idx, dst_pos):
    dst_img.putpixel(dst_pos, org_img.getpixel((org_idx, 0)))

nxt = (0, 0)
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dire = directions[0]
for x_len in range(org_img.size[0]):
    copy_pixel(x_len, nxt)
    if nxt[0]+dire[0] >= dst_img.size[0]:
        dire = directions[1]
    elif nxt[1]+dire[1] >= dst_img.size[1]:
        dire = directions[2]
    elif nxt[0]+dire[0] < 0:
        dire = directions[3]
    if sum(dst_img.getpixel((nxt[0]+dire[0], nxt[1]+dire[1]))):
        dire = directions[(directions.index(dire)+1) % 4]
    nxt = (nxt[0] + dire[0], nxt[1] + dire[1])
dst_img.show()
