#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 00:26:52 2026

@author: frankie
Description:
Enter a principle amount of a CD and year to maturity of CD. Determine the
interest rate based on the amount of the principle and maturity (see below).
Calculate first year interest (principle x interest rate). Display principle, interest
rate and the interest amount for first year.
Principle               Years to Maturity   Interest Rate
>$100,000               5                   6%
$50,000 to $100,000     10                  5%
$50,000 to $100,000     5                   4%
Any other principle and years               2%
"""

# Enter information by user
principle = float(input("Enter the principle amount".ljust(30)+": "))
yearToMaturity = int(input("Enter the year to maturity".ljust(30)+": "))

# Checking interest rate

if principle > 100000 and yearToMaturity == 5 :
    interestRate = 0.06
elif principle >= 50000 and principle <= 100000 and yearToMaturity == 10 :
    interestRate = 0.05
elif principle >= 50000 and principle <= 100000 and yearToMaturity == 5 :
    interestRate = 0.04
else:
    interestRate = 0.02
    
# Calculate interest amount
interestAmountForFirstYear = principle * interestRate

# Display the output

print("".ljust(53,"="))
print("Principle".ljust(30),":",f"{principle:20,.2f}")
print("Interest rate".ljust(30),":",f"{interestRate:20,.0%}")
print("Interest amount for first year".ljust(30),":",f"{interestAmountForFirstYear:20,.2f}")