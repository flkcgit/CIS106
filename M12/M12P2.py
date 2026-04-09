#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:49:12 2026

@author: flkc
Write the code for the following problem. Add another array to problem 1 above. This array
should contain exam score for the respective students. That is, the first name goes with the first
score etc. These are called parallel arrays. Also modify the display functions to include exam
score array in addition to the last name array
"""
# Assign last names & Scores
lastNameList=["Chan","Brothers","Kennth","Vara","Blish","Batt","Cho","Gend","Tropp","Herro"]
examScoreList=[90,80,70,60,50,95,85,75,65,55]

# Function for printing the array
def print_array(arr, titleOfList):
    #Print the array
    print(titleOfList)
    print("="*20)
    for val in arr:
        print(val)

# Function for reverse print
def print_reverse_array(arr,titleOfList):
    # Reverse the array
    arr.reverse()
    print_array(arr,titleOfList)

# Function for parallel print
def print_parallel(arr1,arr2,titleOfList):
    print(titleOfList)    
    print("="*35)
    for index in range(len(arr1)):
        print(f"{arr1[index].ljust(30)}{arr2[index]:5n}")
        

# Function for Reverse parallel print        
def print_reverse_parallel(arr1,arr2,titleOfList):
    arr1.reverse()
    arr2.reverse()
    print_parallel(arr1, arr2, titleOfList)
    
def main():
    # Print in Normal order
    print_parallel(lastNameList,examScoreList,f"\nNormal Order \n{"Last Name".ljust(30," ")}{"Score".rjust(5," ")}")
    
    # print reverse list of last name    
    print_reverse_parallel(lastNameList,examScoreList, f"\nReverse Order \n{"Last Name".ljust(30," ")}{"Score".rjust(5," ")}")

main()
