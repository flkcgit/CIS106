#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 21:08:34 2026

@author: KA CHI LO

Decription :
Enter the user’s last name, number of dependents and gross income. Compute
adjusted gross income to be gross income minus dependents times $12000. Next
determine an income tax rate. Adjusted gross incomes over $50,000 have a tax
rate of 20%. Adjusted gross incomes $50,000 or under have a tax rate of 10%.
Once you determine the tax rate, compute income tax to be adjusted gross income
times tax rate. If the income tax is less than 0, set the income tax to $100.
Display last name, gross income, number of dependents, adjusted gross income,
and income tax.
"""

# Define Constant

ALLOWANCE_PER_DEPENDENT = 12000.0
ADJUSTED_GROSS_INCOMES_LEVEL = 50000.0
TAX_RATE_L1 = 0.10
TAX_RATE_L2 = 0.20
MIN_TAX = 100

# Enter information by user

lastName = input("Enter the last name".ljust(31," ")+": ")
noOfDependents = int(input("Enter the number of dependents".ljust(31," ")+": "))
grossIncome = float(input("Enter the gross income".ljust(31," ")+": "))

# Calculate the adjusted gross incomes

dependentsAllowance = ALLOWANCE_PER_DEPENDENT * noOfDependents
adjustedGrossIncomes= grossIncome - dependentsAllowance

# Calculate the income tax

if adjustedGrossIncomes < ADJUSTED_GROSS_INCOMES_LEVEL :
        incomeTax = adjustedGrossIncomes * TAX_RATE_L1
else:
        incomeTax = adjustedGrossIncomes * TAX_RATE_L2
        
if incomeTax < 0:
    incomeTax = MIN_TAX
    
print("".ljust(43,"="))
print("Income Tax".ljust(30," "),": ",lastName)
print("Gross Income".ljust(30," "),":","{:10.2f}".format(grossIncome))
print("Number of dependents".ljust(30," "),":","{:10.0f}".format(noOfDependents))
print("Adjusted Gross Income".ljust(30," "),":","{:10.2f}".format(adjustedGrossIncomes))
print("Income Tax".ljust(30," "),":","{:10.2f}".format(incomeTax))

    


