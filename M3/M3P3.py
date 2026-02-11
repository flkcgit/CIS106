#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 15:05:29 2026

@author: Ka Chi Lo
Description: You and two friends completed a job and received an amount that is entered into the problem.
You are to split the amount received evenly between the three of you. Compute and display
what each of you will receive.
"""
print("Enter the name of 1st of 2 friends")
firstFriend = str(input())

print("Enter the name of 2nd of friends")
secondFriend = str(input())

print("Enter the received job amount")
amount = float(input())

evenAmount = amount / 3

print(f"Job amount received is ${amount:.2F} and splited as at follows:")
print(f"{firstFriend}: ${evenAmount:,.2F}")
print(f"{secondFriend}: ${evenAmount:,.2F}")
print(f"You: ${evenAmount:,.2F}")
