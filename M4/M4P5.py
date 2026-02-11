#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 00:34:19 2026

@author: KA Chi Lo
Description : You are setting up a business and need to compute the break-even point. This indicates how
many items you must sell at a given price to cover your overhead. Enter fixed costs, price per
unit and cost per unit into your program. Compute the break-even point by dividing fixed costs
by the difference of price per unit and cost per unit.
"""

fixedCosts = float(input("Enter fixed cost".ljust(30,".")+": "))
unitPrice = float(input("Enter price per unit".ljust(30,".")+": "))
costPrice = float(input("Enter cost per unit".ljust(30,".")+": "))
breakEvenPoint = fixedCosts / (unitPrice - costPrice)
print(f"The break-even point for items sell is {breakEvenPoint:.0f} units.")
