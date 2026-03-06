# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:18:46 2026

@author: flkc

Description : 
    Allow the user to enter a start value, stop value and increment value from the keyboard. Display
all the numbers from the start value to stop value using the increment value as you proceed.
Use a while loop structure for this problem
"""

start = int(input("Enter start value: "))
stop = int(input("Enter stop value: "))
increment = int(input("Enter increment value :"))
for i in range(start,stop+1,increment):
    print (i)