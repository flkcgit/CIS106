#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 21:48:20 2026

@author: flkc
Description:
    Prompt the user to repeatedly to do the program input (Yes or No)). If they respond Yes, go into
the loop and prompt them for last name, month and sales. Write a function to compute next
month’s forecast. Pass to the function month and sales. Determine the forecast percent (see
below) and compute next month’s sales to be sales x (1+forecast percent). Return next month’s
sales and display the value.
Month Forecast Percent
Jan, Feb, Mar 0.10
Apr, May, Jun 0.15
Jul, Aug, Sep 0.20
Oct, Nov, Dec 0.25
"""


ans = "Yes"

def compute_forecast(month,sales):
    if month >= 1 and month <= 3:
        forecastPrecent = 0.1
    elif month >= 4 and month <= 6:
        forecastPrecent = 0.15
        
    elif month >= 7 and month <= 9:
        forecastPrecent = 0.20
    else:
        forecastPrecent = 0.25
        
    return sales * (1 + forecastPrecent)

while ans.upper() == "YES":
    lastName = input(f"{"Enter the last name":<30} : ")
    month = 0
    while month < 1 or month > 12:        
        month = int(input(f"{"Enter the month (1-12)":<30} : "))
    sales = float(input(f"{"Enter the sales":<30} : "))
    print(f"{"The next month's sales":<30} : {compute_forecast(month, sales):,.2f}\n")
    ans = input("Whether want to do this program (Yes/No): ")
    
    



