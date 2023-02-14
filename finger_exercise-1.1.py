# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 01:15:56 2023

@author: stoner69
"""

#conditionals ---- if-else

'''Finger Exercise -- Write a program that examines three variables-x, y, and z-
                       and prints the largest odd number among them. If none 
                       of them are odd, it should print a message to that effect. '''
                       
x = 101
y = 111
z= 1341

if x % 2 == 1:
    if y % 2 == 1:
        if z % 2 == 1:
            if z > y:
                if z > x:
                    print(z, "is the largest odd")
                else:
                    print (x, "is the largest odd")
            else:
                if y > x:
                    print(y, "is the largest odd")
                else:
                    print (x, "is the largest odd")
        else:
            if y > x:
                print(y, "is the largest odd")
            else:
                print (x, "is the largest odd")
    else:
        print(x, "is the largest odd")
            

elif y % 2 == 1:
    if z % 2 == 1:
        if z > y:
            print (z, "is the largest odd")
        else:
            print (y, "is the largest odd")
    else:
        print (z, "is the largest odd")
        
elif z % 2 == 1:
    print (z, "is the largest odd")
    
else:
    print ("none of the numbers is an odd")