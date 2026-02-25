#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 19:46:24 2026

@author: Ka Chi Lo
Description :
The warranty of an appliance depends on the cost of the appliance. For appliances
over $1,000 the warrantee cost is 10% of the price. For appliances $1,000 or less
the warranty cost is 5% of the price. The user will enter the name and cost of an
appliance. Display name and cost of appliance, the cost of the warrantee and the
total (cost of the appliance + warranty).    
"""

# Declare Const
WARRANT_LEVEL = 1000
WARRANT_RATE_L1 = 0.10
WARRANT_RATE_L2 = 0.05

# User Inpute Variables

applianceName = input("Enter the Appliaance Name".ljust(40," ")+": ")
applianceCost = float(input("Enter the cost of an appliance".ljust(40," ")+": "))

# Calcuate the Warrantee cost

if applianceCost <= WARRANT_LEVEL:
    warranteeCost = applianceCost * WARRANT_RATE_L2
else:
    warranteeCost = applianceCost * WARRANT_RATE_L1

# Print out the result
print("".ljust(33,"="))
print("Appliance Name".ljust(20," "),":",applianceName)
print("Appliance Cost".ljust(20," "),":","{:10.2f}".format(applianceCost))
print("Warrantee Cost".ljust(20," "),":","{:10.2f}".format(warranteeCost))

