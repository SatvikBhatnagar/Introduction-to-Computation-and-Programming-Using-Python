#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:24:54 2023

@author: stoner69
"""


'''Finger Exercise -- Replace teh comment in the following code with a while loop'''

"""
numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
#concatenate X to toPrint numXs times
print(toPrint)
"""

numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
while numXs != 0:
    toPrint = toPrint + 'X'
    numXs -= 1
print(toPrint)