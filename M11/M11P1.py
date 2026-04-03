#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 20:14:11 2026

@author: flkc
Create a loop that uses a signal (see previous lesson on loops) to stop. In all the problems user entries
are done repeatedly (in a loop) until the signal.
1. Allow the user to enter quantities and prices in a loop. 
2. Use a function to compute the total(quantity times price). 
3. The function should be passed the quantity and price and then return the total. 
4. In the function, provide a 10% discount if the total is over $10,0000.00. 
5. Display quantity, price and total. Sum and display the total extended price.

Input 
Arguments:
Qty, unitprice

Process 
Function:
Compute the extended price, quantity times
unit price.

Output
Return:
Extended price

Input
qty , price from user 

Process
Read user input and compute extended price 

Output
Qty, price, Extprice for
each item
totalExtPrice for all items
"""

ans = "YES"
totalExtendedPrice = 0.0

def compute_expended_price(quantity, unitPrice):
    discount = 0.1
    total = quantity * unitPrice
    if total > 10000:
        total = total * (1 - discount)
    return total
    

while ans.upper() == "YES":
    qty = int(input(f"{"Enter the quantity: ":<30}"))
    price = float(input(f"{"Enter the unit price: ":<30}"))
    extendedPrice = compute_expended_price(qty, price)
    totalExtendedPrice += extendedPrice
    print(f"Quantity : {qty:10,}| Price : {price:10,.2f}| Extended Price : {extendedPrice:10,.2f}\n")
    ans = input("Whether want to do this program (Yes/No): ")

print(f"\nTotal extended price is {totalExtendedPrice:,.2f}.")