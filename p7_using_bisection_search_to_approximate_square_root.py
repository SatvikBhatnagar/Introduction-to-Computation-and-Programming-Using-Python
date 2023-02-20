#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 03:41:48 2023

@author: stoner69
"""

x = 25
epsilon = 0.01
numGusses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans, 'ans**2 =', ans**2)
    numGusses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGusses =', numGusses)
print(ans, 'is close to square root of', x)