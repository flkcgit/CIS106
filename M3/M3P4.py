#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 15:19:06 2026

@author: Ka Chi Lo
Description: Enter the make, model, msrp amount and discount percent of an auto you are interested in.
Compute the amount off msrp you will receive as well as the discounted price. The amount off is
computed to be the msrp times the discount percent (you can enter as a decimal so no need to
divide by 100). The discounted price is the msrp minus the amount off. Display the make, model,
mrsp, discount percent, amount off and discounted price.
"""
print("Enter the make")
make = str(input())
print("Enter the model")
model = str(input())
print("Enter the msrp")
msrp = int(input())
print("Enter the discount percent (as at decimal)")
discount = float(input())
amountOff = msrp * discount
discountPrice = msrp - amountOff

print("The information of auto:")
print(f"Make: {make}")
print(f"Model : {model}")
print(f"MSRP : ${msrp:,.2F}")
print(f"Discount percent : {discount*100:.0F}%")
print(f"Amount Off : ${amountOff:,.2F}")
print(f"Discounted Price : ${discountPrice:,.2F}")

