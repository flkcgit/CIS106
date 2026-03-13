#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 23:35:03 2026

@author: flkc
Description:
    Create a text file that contains employee last name and salary. Read in this data. Determine the
bonus rate based on the chart below. Use that rate to compute bonus. For each line display the
employee’s last name, salary and bonus. After the loop display the sum of all bonuses paid out.
Salary              Bonus Rate
100,000.00 and up       20%
50,000.00               15%
All other salaries      10%
Example file (create your own data with at least 5 employees:
Adams
50000.00
Baker
75000.00
Smith
45000.00
etc.
"""
FILENAME="M8P3Data.txt"

print("Employee's last name     Salary   Bonus")
f = open(FILENAME, 'r')
while True:
    line  = f.readline().rstrip('\n')
    if not line:
        break            
    employeeLastName = line
    salary = line  = float(f.readline().rstrip('\n'))
    if salary >= 100000:
        bonusRate = 0.2
    elif salary == 50000:
        bonusRate = 0.15
    else:
        bonusRate = 0.1    
    print(f"{employeeLastName.ljust(20," ")} {salary:10,.2f}     {bonusRate:.0%}")
f.close
    
    