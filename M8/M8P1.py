# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:35:41 2026

@author: flkc
Description:
    Allow the user to enter a principal amount and interest rate. Repeatedly (need a loop to control
the program execution) compute the annual interest (principle x rate). Compute ending balance
to be principal (beginning balance + interest). Display year, beginning balance and ending
balance for each of the first 5 years. Display the accumulated interest for the 5 years. Note: the
new balance by year (this will be the principle for the following year. Format the output to look
like the example below.
Example:
Enter principal amount: 10000.00
Enter interest rate: 0.10
Formatted output
Year Beginning Ending
Balance Balance
1 $10,000.00 $11,000.00
2 $11,000.00 $12,100.00
3 $12,100.00 $13,310.00
4 $13,310.00 $14,641.00
5 $14,641.00 $16,105.00
Total interest earned: $6,156.00
"""

principleAmount = 0.0
interestRate = 0.0
annualInterest = 0.0
accumlatedInterest = 0.0
NO_OF_YEAR = 5

# User Enter the value
principleAmount = float(input("Enter a principal amount: "))
interestRate = float(input("Enter a interest rate: "))
print("Year:   Beginning     Ending")
print("          Balance    Balance")
print("".ljust(28,"-"))

for i in range(NO_OF_YEAR):
    # Calculate annual interest and print out
    annualInterest = principleAmount * interestRate
    print(f"{i+1:4.0f}   {principleAmount:10,.2f} {principleAmount + annualInterest:10,.2f}")
    
    # Calculate the accumlated Interest and update the principle amount for next year
    accumlatedInterest += annualInterest
    principleAmount += annualInterest

# Print out the accumlated interest
print(f"Total interest earned: ${accumlatedInterest:10,.2f}")