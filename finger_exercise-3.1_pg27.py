#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 19:57:34 2023

@author: stoner69
"""

"""Finger Exercise -- Write a program that asks the user to enter an integer and
                    prints two integers, root and pwr, such that 0 < pwr < 6 and
                    root**pwr is equal to the integer entered by the user. If 
                    no such pait of integer exists, it should print a message to
                    that effect."""
            
num = int(input("Enter an integer: "))
pwr = 4
print ("power:", pwr)
root = 0
while root**pwr < abs(num):
    root = root + 1
if root**pwr != num:
    print("No integer exists such that any integer raised to the power", pwr, "is equal to", num)
else:
    if num < 0:
        num = -num
    print("The given input is equal to ", root, "*", pwr)
