#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 21:04:11 2026

@author: frankie
description: 
    Enter players last name, number of hits and at bats at the keyboard. Use a function to compute
batting average. Pass the hits and at bats to the function. The function should return batting
average. Display last name and batting average. Give a count of the number of players entered.
"""

ans = "Yes"
totalPlayer = 0

def compute_batting_average(hits,bats):
    return hits/bats

while ans.upper() == "YES":
    lastName = input(f"{"Enter the player last name":<30} :") 
    noOfHits = int(input(f"{"Enter the number of hits":<30} :"))
    atBats = int(input(f"{"Enter the at bats":<30} :"))
    print(f"The batting average for {lastName} is {compute_batting_average(noOfHits,atBats):,.2f}.\n")
    totalPlayer += 1
    ans = input("Whether want to do this program (Yes/No): ")
                       
print(f"\nThe number of players is {totalPlayer}.")