#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 19:50:18 2023

@author: stoner69
"""

#Exhaustive Enumeration
"""The algorithmic technique used in this program is a variant of guess 
    and check called exhaustive enumeration. We enumerate all possibilities
    until we get to the right answer or exhaust the space of possibilities."""
    
#Find the cube root of a perfect cube
x = int(input("Enter an integer: "))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)