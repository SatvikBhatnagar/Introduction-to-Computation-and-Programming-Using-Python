#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 17:39:42 2023

@author: stoner69
"""

'''Finger Exercise -- Write a program that asks the user to input 10 integers,
                        and then prints the largest odd number that was entered. 
                        If no odd number was enetered, it should print a message 
                        to that effect.'''
                        
x = 0
odd = False
largest_num = 0
print("Input 10 numbers")
while x != 10:
    num = int(input("Enter a number "))
    if num % 2 == 1:
        odd = True
        if num > largest_num:
            largest_num = num
    x += 1
    
if odd == True:
    print("The largest odd number entered is ", largest_num)