#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:35:23 2026

@author: flkc
Description:
    Write the code for the following problem. Create a dictionary with student name as the key and
the grade as the value. Print student names and grades and class average grade in two columns
with a header for each column
    
"""

scores={"Chan":90,
        "Brothers":80,
        "Kennth":70,
        "Vara":60,
        "Blish":50,
        "Batt":95,
        "Cho":85,
        "Gend":50,
        "Tropp":95,
        "Herro":55
        }

def print_dicionary(dic1,titleOfList):
    total = 0
    print(titleOfList)
    print("="*35)
    for key, val in dic1.items():
        print(f"{key.ljust(30)}{val:5n}")
        total += val
    print("="*35)
    print(f"{"Average".ljust(30)}{total/len(dic1):5n}")
        
        
def main():
    print_dicionary(scores, f"\n{"Last Name".ljust(30," ")}{"Score".rjust(5," ")}")
    
    
main()