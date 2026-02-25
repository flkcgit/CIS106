#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 23:20:23 2026

@author: Ka Chi Lo
Description :
The input to the problem is quantity of widgets. Your program should determine
the price to charge based on the schedule below. Calculate the extended price
(quantity x price). Calculate tax at 7%. Display the extended price, tax amount
and total.
Quantity Price
>10000 $10
5000 to 10000 $20
Below 5000 $30
"""

# Define Constant
TAX_RATE = 0.07


# Enter the information by user

quantity = int(input("Enter the quantity of widgets".ljust(30," ")+": "))

# Check the price
if quantity > 10000:
    price = 10
elif quantity >= 5000 and quantity <= 10000:
    price = 20
else:
    price = 30


# Calculate total

extendedPrice = price * quantity
tax = extendedPrice * TAX_RATE
total = extendedPrice + tax

# Display the output

print("".ljust(53,"="))
print("Extended price".ljust(30," "),":","{:20,.2f}".format(extendedPrice))
print("Tax amount".ljust(30," "),":","{:20,.2f}".format(tax))
print("Total".ljust(30," "),":","{:20,.2f}".format(total))
