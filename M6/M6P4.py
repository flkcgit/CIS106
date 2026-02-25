#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 00:44:41 2026

@author: Ka Chi Lo
Description :
Have the user to enter number of concert tickets. The price per ticket depends on
the volume (see below). Display the number of tickets, price per ticket and the
total cost (number of tickets x Price Per Ticket).
Quantity    Price Per Ticket
>=25        $50
10 to 24    $60
5 to 9      $70
Less 5      $75
"""

# Enter information by user
quantity = int(input("Enter the number of tickets".ljust(30)+":"))

# Check the ticket price
if quantity >= 25:
    price = 50
elif quantity >= 10 and quantity <= 24:
    price = 60
elif quantity >= 5 and quantity <= 9:
    price = 70
else:
    price = 75

# Calcuate the total cost
totalCost = price * quantity

# Display output

print("".ljust(43,"="))
print("Number of tickets".ljust(30),":",f"{quantity:10,.0f}")
print("Price per ticket".ljust(30),":",f"{price:10,.2f}")
print("Total cost".ljust(30),":",f"{totalCost:10,.2f}")