#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:49:12 2026

@author: flkc
Write the code for the following problem. Assign 10 last names to an array. Write a function to
display the names. Write another function to display the names in reverse order
"""
# Assign last name
lastNameList=["Cheng",
          "Chan",
          "Wong",
          "Chen",
          "Lee",
          "Chung",
          "Mok",
          "Yu",
          "Tang",
          "Ho"]

# function for printing the array
def print_array(arr, titleOfList):
    #Print the array
    print(titleOfList)
    print("="*20)
    for val in arr:
        print(val)
        
def print_reverse_array(arr,titleOfList):
    # Reverse the array
    arr.reverse()
    print_array(arr,titleOfList)
        
    
def main():
    # Print in Normal order
    print_array(lastNameList,"\nNormal order\nLast Name")
    
    # print reverse list of last name    
    print_reverse_array(lastNameList, "\nReverse order\nLast Name")

main()
