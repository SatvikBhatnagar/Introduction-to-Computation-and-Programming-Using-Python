#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:32:48 2023

@author: stoner69
"""

#Find a positive integer that is divisible by both 11 and 12
x = 1
while True:
    if x%11 == 0 and x%12 ==0:
        break
    x = x + 1
print(x, 'is divisible by 11 and 12')