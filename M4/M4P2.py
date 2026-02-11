#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 23:11:16 2026

@author: Ka Chi Lo
Description : Input the purchase price per share, the current stock price and quantity of stock, compute the
increase (or decrease) of the value of the stock entered. (Value is computed as (current price –
price per share) * quantity. If the amount is negative that means you are losing money).
"""

purchasePrice = float(input("Enter the purchase price per share ".ljust(50," ") + ":"))
currentPrice = float(input("Enter the current stock price ".ljust(50," ") + ":"))
quantity = float(input("Enter the quantity of stock ".ljust(50," ") + ":"))
changeInValue = (currentPrice - purchasePrice) * quantity

print("Increase (or decrease) of the value of stock ".ljust(50," ") + ":","{:10.2f}".format(changeInValue))
