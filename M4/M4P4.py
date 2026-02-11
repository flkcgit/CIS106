#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 00:27:04 2026

@author: Ka Chi Lo
Description: Enter first name and number of steps walked in a day. For each step you burned .25 calories.
Computer the number of calories burned. Display first name and calories burned.
"""

caloriesBurnedRate = 0.25
firstName = input("Enter the first name".ljust(45," ")+": ")
steps = int(input("Enter the number of steps walked in a day".ljust(45," ")+": "))
caloriesBurned = steps * caloriesBurnedRate
print(f"{firstName} burned {caloriesBurned:0.2f} calories.")
