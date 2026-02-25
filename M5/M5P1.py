# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 19:26:54 2026

@author: Ka Chi Lo
Description: Allow a user to enter a quantity of an item. If the quantity is greater than or equal
to 1000, the unit price should be $3.00. For quantities under 1000 the unit price is
$5.00. Compute extended price to be quantity x unit price. Compute tax to be 7%
of the extended price. The total is computed as extended price plus the tax.
Display the quantity, unit price, extended price, tax and total
"""

TAX_RATE = 0.07

# Get Quantity from user
qty = int(input("Enter quantity :"))

if qty >= 1000:
    price = 3.0
else:
    price = 5.0
    
extendedPrice = qty * price
tax = extendedPrice * TAX_RATE
total = extendedPrice + tax
print("".ljust(33,"="))
print("Quantity".ljust(20," "),":","{:10.0f}".format(qty))
print("Unit Price".ljust(20," "),":","{:10.2f}".format(price))
print("extenedPrice".ljust(20," "),":","{:10.2f}".format(extendedPrice))
print("Tax".ljust(20," "),":","{:10.2f}".format(tax))
print("Total".ljust(20," "),":","{:10.2f}".format(total))