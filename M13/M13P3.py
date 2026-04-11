#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:28:06 2026

@author: flkc
Description:
    Load list of 10 Player Names and Batting Averages from a file into a dictionary. (Create your own
file with two items: player last name and batting average, i.e. 0.267, 0.300 etc, or use the file
you created in the earlier problem set). Write a function to print the dictionary contents in two
columns with a header for the name and average.
"""

FILENAME = "M13P3 Data.txt"

def load_data_to_dictionary(filename):
    # Declare dictionary
    dic1 = {}    
    
    with open(filename, 'r') as f:
        while True:
            tmp1 = f.readline().rstrip("\n")
            if not tmp1:
                break;
                
            # Add to Dictionary        
            dic1[tmp1] = float(f.readline().rstrip("\n"))        
        return dic1


def print_dicionary(dic1,titleOfList):
    total = 0
    print(titleOfList)
    print("="*45)
    for key, val in dic1.items():
        print(f"{key.ljust(30)}{val:15.2f}")
        total += val
    #print("="*45)
    #print(f"{"Average".ljust(30)}{total/len(dic1):15.2f}")


def main():
    players = load_data_to_dictionary(FILENAME)
    print_dicionary(players, f"\n{"Player Last Name".ljust(30," ")}{"Batting Average".rjust(15," ")}")
    
main()