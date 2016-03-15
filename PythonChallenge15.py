#!/usr/bin/python
# encoding:utf-8
# -*- Mode: Python -*-
# Author: Soros Liu <soros.liu1029@gmail.com>

# ==================================================================================================
# Copyright 2016 by Soros Liu
#
#                                                                          All Rights Reserved
"""
Use datetime module to match the missing calendar
"""
import datetime
__author__ = 'Soros Liu'

flag = False
for mid_year in range(99, -1, -1):
    year = 1000 + mid_year * 10 + 6
    guess_day = datetime.date(year, 1, 26).isoweekday()
    if guess_day == 1 and not year % 4:
        print(year)
        if flag:
            print(year)
            exit(0)
        else:
            flag = True
