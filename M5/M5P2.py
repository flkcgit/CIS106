# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 20:00:05 2026

@author: Ka Chi Lo
Description :
The program asks the user for an item and quantity. Determine the unit price of
the item based on the chart below. Compute the extended price to be quantity x
unit price. Display the item, unit price and extended price. Note: if the item
entered is not A then assume the item is B. No need to check for B.
Item Unit Price
A $10.00
B $20.00
(Note: assume the user will enter the data correctly. Assume if they enter capital
A then $10.00 gets assigned to unit price variable. Any other entry is assumed to
be a capital B whether they enter B or not. Therefore, you only need a relational
condition for A. This makes the if statement easier and removes data validation
from the program which could get quite complex).
if item == “A”:
Unit_price = 10.00
else:
Unit_price = 20.00    
"""

item = input("Enter the Item : ")
qty = int(input("Enter the quantity : "))
if item == "A":
    unitPrice = 10.00
else:
    unitPrice = 20.00
    item = "B"

extendedPrice = qty * unitPrice

print("".ljust(33,"="))
print("Item".ljust(20," "),":",item.rjust(10," "))
print("Unit Price".ljust(20," "),":","{:10.2f}".format(unitPrice))
print("Extended Price".ljust(20," "),":","{:10.2f}".format(extendedPrice))