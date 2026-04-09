#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:49:12 2026

@author: flkc
Write the code for the following problem. The data to load is lastname and score. You can do
this from a file as done in an earlier exercise. Add a function to the program to display the last
name and highest score, last name and lowest score.
"""

FILENAME = "M12P3 Data.txt"
lastNameList = []
examScoreList = []

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

# Function for loading data
def load_data():
    # Declare List 1 and list 2
    list1 = []
    list2 = []
    
    f = open(FILENAME, 'r')
    while True:
        tmp1 = f.readline().rstrip("\n")
        if not tmp1:
            break;
        # Append to list1
        list1.append(tmp1)
        tmp2 = float(f.readline().rstrip("\n"))
        
        # Append to Score List
        list2.append(tmp2)
    return list1, list2
    f.close()

# Compare and Find the Highest/Lowest scores
def compare_score(names,scores,isHighest = True):
    
    lastScoreIndex = []
    lastScoreIndex.append(0)
    
    # Set the flag = 1 if searching highest score else flag = -1
    flag = 1 if isHighest else -1
    
    # Compare the score with latest Highest/Lowest score
    for index in range(1,len(scores)):        
        if scores[index] * flag > scores[lastScoreIndex[0]] * flag:
            
            # if new Highest/Lowest score find, replace the old list
            lastScoreIndex.clear()
            lastScoreIndex.append(index)      
            
        elif scores[index] * flag == scores[lastScoreIndex[0]] * flag:
            
            # if more then one Highest/Lowest Scores, append into the list
            lastScoreIndex.append(index)
            
        

    # Display the result
    print(f"\n{"Highest" if isHighest else "Lowest"} Score")
    print(f"{"Last Name".ljust(30," ")}{"Score".rjust(5," ")}")    
    print("="*35)
    for index in lastScoreIndex:
        print(f"{names[index].ljust(30)}{scores[index]:5n}")
        
    
        
    
def main():
    lastNameList,examScoreList = load_data()   
    
    # Print in Normal order
    print_parallel(lastNameList,examScoreList,f"Normal order\n{"Last Name".ljust(30," ")}{"Score".rjust(5," ")}")
    
    # print reverse list of last name    
    print_reverse_parallel(lastNameList,examScoreList, f"\nReverse order\n{"Last Name".ljust(30," ")}{"Score".rjust(5," ")}")
    
    # Find the Highest Score    
    compare_score(lastNameList, examScoreList, True)
    
    # Find the Lowest Score
    compare_score(lastNameList, examScoreList, False)
    
    
    
    

main()
