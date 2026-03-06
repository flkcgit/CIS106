#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 01:11:43 2026

@author: flkc
Description:
    Prompt the user on whether they want to do this program (just before the while loop). Yes
means they want to continue. Any other response indicates they will stop the program. This
response is the loop control variable. If the user answers Yes then go into the while loop.
Note: you may use any variation or yes as shown in class to continue.
Once in the while loop. You are to prompt the user for quantity and price of an item. Compute
extended price (quantity times price of an item. If the extended price is greater than 10000.00
compute a discount of 25%. All other orders get a 10% discount. For each order display
extended price, discount amount (extended price x discount percent), total (extended price –
discount amount).
For each order sum the discount amount.
After the loop (all data entered) display the sum of all the discounts.
Finally, the last statements within the while loop will ask the user if they want to do this loop
again. In other words, the user needs to be prompted again. The reason is that the end of the
loop takes execution to the while condition to be evaluated again. It cannot take us to the first
few lines of code that prompt the user for the first time. That code is out of the loop. Therefore,
we need a second prompt at the bottom, inside the loop.
"""


quantity = 0
price = 0.0
extendedPrice = 0.0
SPECIAL_DISCOUNT = 0.25
STANDARD_DISCOUNT = 0.1
discoount = 0.0
total = 0.0
sumOfDiscount = 0.0


ans = input("Whether want to do this program (Yes/No): ")

while ans == "Yes":        
    quantity = int(input("Enter the quantity: "))
    price = float(input("Enter the price: "))
    # Calucate extended Price
    extendedPrice = quantity * price
    if extendedPrice > 10000:
        discount = extendedPrice * SPECIAL_DISCOUNT
    else:
        discount = extendedPrice * STANDARD_DISCOUNT
    total = extendedPrice - discount
    print(f"\nExtended price:     {extendedPrice:10.2f}")
    print(f"Discount amount:    {discount:10.2f}")
    print(f"Total:              {total:10.2f}")
    print("------------------------------\n")    
    sumOfDiscount += discount
    ans = input("Whether want to do this program (Yes/No): ")


print(f"Sum of the discount:   {sumOfDiscount:10.2f}")
