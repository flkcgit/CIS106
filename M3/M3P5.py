#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 15:31:52 2026

@author: Ka Chi Lo
Description: Allow the user to enter a radius of a circle. Compute and display the area to be pi times radius
squared (use 3.14 for pi and multiple radius time radius for radius squared). Also, compute and
display the perimeter (2 times pi * radius).
"""

print("Enter the radius of a circle")
radius = float(input())
pi = 3.14
area = pi * radius * radius
perimeter = 2 * pi * radius
print(f"The radius is {radius:.2F}, the area is {area:.2F}, the perimeter is {perimeter:.2F}.")