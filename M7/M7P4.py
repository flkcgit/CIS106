#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 00:49:47 2026

@author: flkc
Description:
    Prompt the user on whether they want to do this program (just before the while loop). Yes
means they want to continue. Any other response indicates they will stop the program. This
response is the loop control variable. If the user answers Yes then go into the while loop.
Note: you may use any variation or yes as shown in class to continue.
Once in the while loop. You are to prompt the user for employee last name, hours worked and
rate of pay. Compute gross pay. Give the employee time and a half for hours worked over 40.
Sum the gross pay and count the number of employees.
For each employee display their last name and gross pay.
After the loop (all data entered) display the sum of all the gross pays, and count of the number
of employees. Compute and display the average pay.
Finally, the last statements within the while loop will ask the user if they want to do this loop
again. In other words, the user needs to be prompted again. The reason is that the end of the
loop takes execution to the while condition to be evaluated again. It cannot take us to the first
few lines of code that prompt the user for the first time. That code is out of the loop. Therefore,
we need a second prompt at the bottom, inside the loop.
"""

lastName = ""
hoursWorked = 0
rateOfPay = 0.0
noOfEmployee = 0
grossPay = 0.0
sumOfGrossPays = 0.0
averagePay = 0

ans = input("Whether want to do this program (Yes/No): ")

while ans == "Yes":    
    lastName = input("Enter the employee last name: ")
    hoursWorked = float(input("Enter the hours worked: "))
    rateOfPay = float(input("Enter the rate of pay: "))
    # Calucate gross pay
    if hoursWorked > 40:
        grossPay = (hoursWorked-40) * rateOfPay * 1.5 + 40 * rateOfPay
    else:
        grossPay = hoursWorked * rateOfPay
    
    print(f"\nLast name:     {lastName}")
    print(f"Gross Pay: {grossPay:3.2f}")
    print("---------------------------------\n")
    noOfEmployee += 1
    sumOfGrossPays += grossPay
    ans = input("Whether want to do this program (Yes/No): ")

averagePay = sumOfGrossPays / noOfEmployee
print(f"Sum of gross pays:   {sumOfGrossPays:10.2f}")
print(f"Number of employees: {noOfEmployee:10.0f}")
print(f"Average pay:         {averagePay:10.2f}")


