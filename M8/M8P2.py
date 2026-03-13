#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 23:17:59 2026

@author: flkc
Description:
    Fibonacci sequence is a sequence of natural order. The sequence is:
1, 1, 2, 3, 5, 8 etc. where it is a series of numbers that may start with 0 and 1, and each
subsequent number is the sum of the two preceding numbers. For this exercise, start with 1.
Use a for loop compute and display first 20 numbers in the sequence
"""

NO_OF_NUMBER = 20
x1 = 0
x2 = 1
fibonacci = 1
print("No  Fibonacci")
for x in range(0,NO_OF_NUMBER,1) :        
    print(f"{x+1:2.0f}      {fibonacci:5.0f}")
    fibonacci = x1 + x2    
    x1 = x2
    x2 = fibonacci
    
    
    
    