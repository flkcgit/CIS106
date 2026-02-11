#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 14:50:22 2026

@author: Ka Chi Lo
Description: The student will enter their last name, midterm and final exam scores (0 – 100 points). Compute
the total exam points to be the sum of 40% of midterm and 60% of the final exam. Display
student last name and total exam points.
    
"""
print("Enter the last name")
lastName = str(input())
print("Enter the midterm score (0-100 points)")
midterm = int(input())
print("Enter the final exam score (0-100 points)")
final = int(input())

if midterm < 0 or midterm > 100:
    print("Error: The midterm score must between 0 to 100")
    
if final < 0 or final >100:
    print("Error: The final exam score must between 0 to 100")
    
if (final >= 0 and final <= 100 and midterm >=0 and midterm <= 100):
    totalExam = midterm * 0.4 + final * 0.6
    print(f"{lastName}: total exam point is {totalExam}.")
    