#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 00:07:44 2026

@author: flkc
Description:
    Create a text file with item, quantity and price. Read through the file one line at a time.
Compute the extended price (quantity x price). For each line display the item, quantity, price
and extended price. After the loop display the sum of all the extended prices, the count of the
number of orders and the average order.
Example Data File
Widget
10
50
Hammer
2
10
Saw
4
8
etc
"""

FILENAME="M8P4Data.txt"
f = open(FILENAME, 'r')
extendedPrice = 0.0
sumOfExtendedPrice = 0.0
countOfOrder = 0
averageOrder = 0.0

print("Item              Quantity       Price  Extended Price")
while True:
    item = f.readline().rstrip("\n")
    if not item:
        break
    quantity = int(f.readline().rstrip("\n"))
    price = float(f.readline().rstrip("\n"))
    extendedPrice = quantity * price
    print(f"{item.ljust(15," ")} {quantity:10,.0f}  {price:10,.2f} {extendedPrice:15,.2f}")
    sumOfExtendedPrice += extendedPrice
    countOfOrder += 1
    

averageOrder = sumOfExtendedPrice / countOfOrder
print(f"\nTotal extended price : {sumOfExtendedPrice:15,.2f}")
print(f"Number of order :      {countOfOrder:15,.0f}")
print(f"Average order :        {averageOrder:15,.2f}")
