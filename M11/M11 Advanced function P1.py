#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:30:54 2026

@author: flkc
Description:
    The input consists of quantity, price and discount rate. Use a function to compute the discount
amount and discounted price. Then, display these values in the main part of the program, along
with the quantity and price. (The function should return both discount amount and discounted
price)
"""


def compute_discount(quantity,unitPrice,discountRate):
    return quantity * unitPrice * discountRate, quantity * unitPrice * (1 - discountRate)



qty = int(input(f"{"Enter the quantity":<30} : "))
price = float(input(f"{"Enter the price":<30} : "))
discountRate = float(input(f"{"Enter the discount rate":<30} : "))
discountAmount, discountedPrice = compute_discount(qty, price, discountRate)
print("-"*75)
print(f"|{"Quantity":^15}|{"Price":^15}|{"Discount Amount":^20}|{"Discounted Price":^20}|")
print(f"|{qty:^15,}|{price:^15,.2f}|{discountAmount:^20,.2f}|{discountedPrice:^20,.2f}|")
print("-"*75)
    