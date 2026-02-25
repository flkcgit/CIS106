#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 14:53:54 2026

@author: Ka Chi Lo
Enter the number of books to order and cost per book. If the order total is over
$50.00 shipping is free. If the order total is $50.00 or under charge $25 shipping.
Display the order total and shipping charge (note 0 should display for a free
shipping charge)
"""

# Define fixed variable
FREE_SHIPPING_SALES = 50.0
SHIPPING_FEE = 25.0

# Entry variable by user
noOfBook = int(input("Enter the number of books".ljust(31," ")+": "))
costOfbook = float(input("Enter the cost per book".ljust(31," ")+": "))

# Calcuate the total sales & print it
totalSales = noOfBook * costOfbook
print("Order Total".ljust(30," "),":","{:10.2f}".format(totalSales))

# Check Shipping Fee & print it

if totalSales > FREE_SHIPPING_SALES:    
    print("Shipping charge".ljust(30," "),":","Free shipping charge")
else:
    print("Shipping charge".ljust(30," "),":","{:10.2f}".format(SHIPPING_FEE))
