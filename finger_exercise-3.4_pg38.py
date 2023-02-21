#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 12:02:06 2023

@author: stoner69
"""

'''Finger Exercise -- Add some code to the implementation of Newton-Raphson that 
                        keeps track of the number of iterations used to find the 
                        root. Use that code as part of a program that compares the 
                        efficiency of Newton-Raphson and bisection search. '''
                        

epsilon = 0.01
k = 24.0
guess = k/2.0
count = 0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    count += 1
print('///Newton-Raphson Method///')
print('Square root of', k, 'is about', guess)
print('Number of iterations:', count)


print('///Bisection Search///')
x = 25
epsilon = 0.01
numGusses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    numGusses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('Number of iterations', numGusses)
print(ans, 'is close to square root of', x)