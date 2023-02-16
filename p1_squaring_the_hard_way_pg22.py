#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 10:19:45 2023

@author: stoner69
"""

#Square an integer, the hard way
x = 5
ans = 0
itersLeft = x
while (itersLeft != 0):
    ans = ans + abs(x)
    itersLeft = itersLeft - 1
print(str(x) + '*' + str(x) + ' = ' + str(ans))