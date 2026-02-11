#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 16:32:38 2026

@author: Ka Chi Lo
Description : Allow the user to enter two exam scores from the keyboard. 
The first exam is worth 60% of the total points and the second exam is worth 40%. 
Calculate the total score by multiplying each exam score input by the respective weighting 
then add the two results together. Display the total.
"""

examOneWeight = 0.6
examTwoWeight = 0.4
examOne = int(input("Enter the first exam score".ljust(30," ")+": "))
examTwo = int(input("Enter the second exam score".ljust(30," ")+": "))


totalScore = examOne * examOneWeight + examTwo * examTwoWeight
print("Total Exam Score".ljust(30," ")+":","{:10.2f}".format(totalScore))