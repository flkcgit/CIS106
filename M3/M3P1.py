#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 13:38:41 2026

@author: Ka Chi Lo
Description: Allow the user to enter the stock ticker symbol (ie MSFT for Microsoft), number of shares and
cost per share. Compute and display amount invested to be number of shares times cost per
share. 
"""

print("Enter the Stock Ticker Symbol (ie MSFT for Microsoft)")
stockSymbol = str(input())
print("Enter the number of shares")
numberOfShare = int(input())
print("Enter the cost per share")
cost = float(input())
amount = numberOfShare * cost
print(f"Total Amount for {numberOfShare} share(s) of {stockSymbol} is {amount:,.2f}.")
