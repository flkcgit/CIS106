#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 23:23:13 2026

@author: Ka Chi Lo
Description:
    Enter the total for a meal. Compute a tip at 15%, 18% and 20%. Display total, each tip value and
total with each tip value. Your output should have total for the meal as entered, tip and total
with tip for each tip value. (9 lines). Put a blank line between each tip of the set of tip values. For
example, Points are lost if the output is not formatted according to the directions.
With 15% Tip:
Total: 10.00
Tip: 1.50
Total with Tip 11.50
With 18% Tip:
Total: 10.00
Tip: 1.80
Total with Tip 11.80
With 20% Tip:
Total: 10.00
Tip: 2.00
Total with Tip 12.00
"""

tip1Rate = 0.15
tip2Rate = 0.18
tip3Rate = 0.2


mealTotal = float(input("Enter the total for a meal : "))

tip1 = mealTotal * tip1Rate
totalWithTip1 = mealTotal + tip1
tip2 = mealTotal * tip2Rate
totalWithTip2 = mealTotal + tip2
tip3 = mealTotal * tip3Rate
totalWithTip3 = mealTotal + tip3

print(f"With {tip1Rate*100}% Tip:\n")
print("Total".ljust(20," "),":",f"{mealTotal:10.2f}")
print("Tip".ljust(20," "),":",f"{tip1:10.2f}")
print("Total with Tip".ljust(20," "),":",f"{totalWithTip1:10.2f}")
print("\n")
print(f"With {tip2Rate*100}% Tip:\n")
print("Total".ljust(20," "),":",f"{mealTotal:10.2f}")
print("Tip".ljust(20," "),":",f"{tip2:10.2f}")
print("Total with Tip".ljust(20," "),":",f"{totalWithTip2:10.2f}")
print("\n")
print(f"With {tip3Rate*100}% Tip:\n")
print("Total".ljust(20," "),":",f"{mealTotal:10.2f}")
print("Tip".ljust(20," "),":",f"{tip3:10.2f}")
print("Total with Tip".ljust(20," "),":",f"{totalWithTip3:10.2f}")
