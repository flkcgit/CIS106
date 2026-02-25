#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 00:53:55 2026

@author: Ka Chi Lo
The user will enter employee last name, salary and job level (as noted below). Use
the job level to determine the bonus rate. Then compute bonus to be salary times
bonus rate. Display employee last name and bonus.
Job Level       Bonus Rate
10 and above    25%
5 to 9          20%
All others      10%
"""
# Enter information by user
lastName = input("Enter the employee last name".ljust(30)+": ")
salary = float(input("Enter the salary".ljust(30)+": "))
jobLevel = int(input("Enter the job level".ljust(30)+": "))

# Check the bouns rate
if jobLevel >= 10:
    bonusRate = 0.25
elif jobLevel >= 5 and jobLevel <= 9:
    bonusRate = 0.20
else:
    bonusRate = 0.10

# Calcuate the bouns
bonus = salary * bonusRate

# Display output

print("".ljust(43,"="))
print("Employee last name".ljust(30),":",lastName.rjust(10))
print("Bonus".ljust(30),":",f"{bonus:10,.2f}")

