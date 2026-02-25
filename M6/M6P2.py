#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 00:10:28 2026

@author: Ka Chi Lo
Description :
Enter a part number and quantity Determine the cost per unit using the table
below. Then calculate the total cost (quantity x unit cost). Display the part
number, cost per unit and total cost. Note: Part number can be an integer but it can
also be a string because you are not doing arithmetic on it. However, in your code
if statement be sure to compare using consistency, that is, if item == “10” when
item is a string and if item == 10 when item is an integer.
Part Unit Cost
10 or 55 1.00
99 2.00
80 or 70 3.00
All others 5.00
"""

# Enter the information by user
partNumber = input("Enter part number".ljust(30)+": ")
quantity = int(input("Enter quantity".ljust(30)+": "))

# Checking unit cost

if partNumber == "10"  or partNumber == "55":
    unitCost = 1.00
elif partNumber == "99":
    unitCost = 2.00
elif partNumber == "80"  or partNumber == "70":
    unitCost = 3.00
else:
    unitCost = 5.00
    
# Calculate the total cost

totalCost = quantity * unitCost

# Display the output

print ("".ljust(53,"="))
print("Part Number".ljust(30),":",partNumber.rjust(20))
print("Cost per unit".ljust(30),":",f"{unitCost:20,.2f}")
print("Total Cost".ljust(30),":",f"{totalCost:20,.2f}")

