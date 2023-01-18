# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 01:15:56 2023

@author: stoner69
"""

#conditionals ---- if-else

'''Finger Exercise -- Write a program that examines three variables-x, y, and z-
                       and prints the largest odd number among them. If none 
                       of them are odd, it should print a message to that effect. '''
                       
x = 10
y = 11
z= 13

if x % 2 == 1:
    print("x = ", x, "is odd")
elif y % 2 == 1:
    print("y = ", y, "is odd")
elif z % 2 == 1:
    print("z = ", z, "is odd")
else:
    print("none of the numbers are odd")