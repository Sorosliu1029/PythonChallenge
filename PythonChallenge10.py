#!/usr/bin/python
# encoding:utf-8
# -*- Mode: Python -*-
# Author: Soros Liu <soros.liu1029@gmail.com>

# ==================================================================================================
# Copyright 2016 by Soros Liu
#
#                                                                          All Rights Reserved
"""
reference from the Python Challenge community
"""
import re
__author__ = 'Soros Liu'
x = "1"
for each in range(30):
    x = "".join([str(len(i+j))+i for i, j in re.findall(r"(\d)(\1*)", x)])
print(len(x))
