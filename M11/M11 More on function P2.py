#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:44:11 2026

@author: flkc
Description:
    Prompt the user to repeatedly to do the program (input (Yes or No)). If they response Yes go
into the loop and prompt the user for make, model, electric vehicle code (Y or N) and MSRP
(sticker price) of an automobile. 
Write a function to compute the out the door price. Pass to the function the MSRP, make, model and electric vehicle code. 
Determine the percent off the MSRP then compute the new MSRP 
and finally add 7% sales tax to the total. 
Return and display the total. 
Also sum all MSRP’s and sum of all sales price of the cars (MSRP – discount + tax).

To determine percent off MSRP Percent off MSRP
Honda Accord 0.10
Toyota Rav4 0.15
All electric vehicles 0.30
All other vehicles 0.05
"""

ans = "Yes"
allSalesPrice = 0
allMSRP = 0

def compute_out_door_price(msrp,make,model,isElectricVehicle):
    taxRate = 0.07
    if make.upper() == "HONDA" and model.upper() == "ACCORD":
        percentOff = 0.1
    elif make.upper() == "TOYOTA" and model.upper() == "RAV4":
        percentOff = 0.15
    elif isElectricVehicle == "Y":
        percentOff = 0.30
    else:
        percentOff = 0.05
    return msrp * (1 - percentOff) * ( 1 + taxRate)

while ans.upper() == "YES":
    make = input(f"{"Enter the make":<40} : ")
    model = input(f"{"Enter the model":<40} : ")
    isElectricVehicle = ""
    while isElectricVehicle != "Y" and isElectricVehicle != "N":
        isElectricVehicle = input(f"{"Enter the Electric Vehicle Code (Y/N)":<40} : ").upper()
    msrp = int(input(f"{"Enter the MSRP":<40} : "))    
    salesPrice = compute_out_door_price(msrp, make, model, isElectricVehicle)
    print(f"{"The Sales Price ":<40} : {salesPrice:,.2f}\n")
    allSalesPrice += salesPrice
    allMSRP += msrp
    ans = input("Whether want to do this program (Yes/No): ")

print(f"The Total MSRP is {allMSRP:,} and total Sales Price is {allSalesPrice:,.2f}\n")
    