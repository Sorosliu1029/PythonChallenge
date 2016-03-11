#!/usr/bin/python
# encoding:utf-8
# -*- Mode: Python -*-
# Author: Soros Liu <soros.liu1029@gmail.com>

# ==================================================================================================
# Copyright 2016 by Soros Liu
#
#                                                                          All Rights Reserved
"""
Refer to blog: http://www.cnblogs.com/dukeleo/p/3471375.html
"""
from xmlrpc.client import ServerProxy
__author__ = 'Soros Liu'
rpc = ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
# print(rpc)
methods = rpc.system.listMethods()
print(methods)
for method in methods:
    print(method + ' : ' + rpc.system.methodHelp(method))
print(rpc.phone('Bert'))