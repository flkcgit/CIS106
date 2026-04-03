#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:50:30 2026

@author: flkc
Description:
    Enter the student’s last name and 3 exam scores. Use a function to compute the average and
total points. This function should return both total points and average. Display student’s last
name, total points and average exam score.
"""


def compute_scores(exam1, exam2, exam3):
    return (exam1 + exam2 + exam3), (exam1 + exam2 + exam3)/3



lastName = input(f"{"Enter the student\'s last name":<30} : ")
exam1 = int(input(f"{"Enter the exam 1 scores":<30} : "))
exam2 = int(input(f"{"Enter the exam 2 scores":<30} : "))
exam3 = int(input(f"{"Enter the exam 3 scores":<30} : "))

averagePoint, totalPoint = compute_scores(exam1, exam2, exam3)
print("-"*69)
print(f"|{"Student\'s Last Name":^30}|{"Total Points":^15}|{"Average Exam Score":^20}|")
print(f"|{lastName:^30}|{totalPoint:^15,}|{averagePoint:^20,.2f}|")
print("-"*69)
