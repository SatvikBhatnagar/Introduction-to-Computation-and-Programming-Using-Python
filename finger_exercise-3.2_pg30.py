#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 00:23:07 2023

@author: stoner69
"""

"""Finger Exercise -- Let s be a string that contains a sequence of decimal 
                        numbers separated by commas, e.g., s= '1.23,2.4,3.123'.
                        Write a program that prints the sum of the numbers in s."""
                        
s = '1.23,234.1,.'
total = 0
temp = ''

while s[-1] == ',' or s[-1] == '.':
    s = s[0:len(s)-1]

for i in s:
    if i != ',':
        temp = temp + i
    elif i == ',':
        if temp != '':
            total = total + float(temp)
            temp = ''        
        else:
            pass

total = total + float(temp)        
print(total)
                    