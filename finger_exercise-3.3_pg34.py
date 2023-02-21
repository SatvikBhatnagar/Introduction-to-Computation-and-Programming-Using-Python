#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 05:13:52 2023

@author: stoner69
"""

"""Finger Exercise -- What would have to be change to make the code in the bisection-search-approximiation-of-square-root
                        work for finding an approximation to the cube root of both negative and positive numbers?"""
                        
y = -125                      
x = abs(y)
epsilon = 0.01
numGusses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans, 'ans**3 =', ans**3)
    numGusses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGusses =', numGusses)
if y < 0:
    print(-ans, 'is close to cube root of', y)
else:
    print(ans, 'is close to cube root of', y)