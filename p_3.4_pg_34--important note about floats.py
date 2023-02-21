#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 08:01:22 2023

@author: stoner69
"""

x = 0.0
for i in range(10):
    x = x + 0.1
if x == 1.0:
    print(x, '= 1.0')
else:
    print(x, 'is not 1.0')
    
'''In most python implementaions, there are 53 bits of precision available for floating point numbers.'''

'''As could be seen in the result of the above code, using == to compare two floating point values can 
produce a surprising result. IT IS ALWAYS MORE APPROPRIATE TO ASK WHETHER TWO FLOATING POINT VALUES ARE 
CLOSE ENOUGH TO EACH OTHER, NOT WHETHER THEY ARE IDENTICAL.'''

#What actually needs to be done:
if abs(1.0 - x) < 0.001:
    print("The numbers are close enough")
else:
    print("The numbers are not close enough")