#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 00:24:58 2026

@author: flkc
Description:
    Create a text file with student last name, district code (I or O) and number of credits taken.
Compute tuition owed (credits taken x cost per credit). Cost per credit for in district students
(district code I) is 250.00. Out of district students pay 500.00 per credit. For each line display
student last name, credits taken and tuition owed. After the loop display sum of all tuition owed
and the number of students.
Example file
Jones
I
12
Adams
I
10
Baker
O
12
Smith
O
16
"""

FILENAME="M8P5Data.txt"
COST_PER_CREDIT_IN = 250
COST_PER_CREDIT_OUT = 500
f = open(FILENAME, 'r')
tuition = 0.0
sumOfTuition = 0.0
numberOfStudent = 0


print("Student last name   Credit Taken  Tuition owed")
while True:
    student = f.readline().rstrip("\n")
    if not student:
        break
    districtCode = f.readline().rstrip("\n")
    creditTaken  = int(f.readline().rstrip("\n"))
    if districtCode == "I":
        tuition = COST_PER_CREDIT_IN * creditTaken
    else:
        tuition = COST_PER_CREDIT_OUT * creditTaken
    sumOfTuition += tuition
    numberOfStudent += 1
    print(f"{student.ljust(20," ")}  {creditTaken:10,.0f}  {tuition:12,.2f}")

print(f"\nSum of tuition owed :  {sumOfTuition:15,.2f}")
print(f"Number of student :    {numberOfStudent:15,.0f}")

    