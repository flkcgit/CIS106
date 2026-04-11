#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:35:23 2026

@author: flkc
Description:
    Write the code for the following problem. Expand the dictionary above to have a list of three
grades as the value. Create a function to create a list of three grade averages for the class. This
list may be a dictionary, a list of lists ([name, average] as each element of the list, or some other
list structure of your choice.
Print the list of students and their grade averages. Also print the class average for each of the
three grades. Layout the output for ease of readability by the use
    
"""

scores={"Chan":[80,90,70],
        "Brothers":[85,60,70],
        "Kennth":[80,91,73],
        "Vara":[84,94,70],
        "Blish":[70,79,75],
        "Batt":[84,90,74],
        "Cho":[83,90,73],
        "Gend":[82,90,78],
        "Tropp":[80,70,75],
        "Herro":[81,94,80]
        }

def print_dicionary(dic1,titleOfList):
    total = 0
    print(titleOfList)
    print("="*45)
    for key, val in dic1.items():
        print(f"{key.ljust(30)}{val:15.2f}")
        total += val
    print("="*45)
    print(f"{"Average".ljust(30)}{total/len(dic1):15.2f}")


def grade_average(dic1):
    dic2= {}
    for key, values in dic1.items():
        total = 0
        for val in values:
            total += val            
        dic2[key] = total/len(values)
    return dic2
        
def main():
    #print_dicionary(scores, f"\n{"Last Name".ljust(30," ")}{"Score".rjust(5," ")}")
    average_scores = grade_average(scores)
    print_dicionary(average_scores, f"\n{"Last Name".ljust(30," ")}{"Average Grade".rjust(15," ")}")
    
    
main()