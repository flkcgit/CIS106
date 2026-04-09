#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:02:01 2026

@author: flkc
Description:
    Copy and modify 4 above to display a message, “Name not found” when the name is not in the
list.
"""

FILENAME = "M12P4 Data.txt"
playerNameList = []
battingAvgList = []

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
    
# Function for parallel print
def print_parallel(arr1,arr2,titleOfList):
    print(titleOfList)    
    print("="*35)
    for index in range(len(arr1)):
        print(f"{arr1[index].ljust(30)}{arr2[index]:5n}")
        
def search_name(searchText, arr1, arr2,titleOfList):        
    searchText = searchText.upper()
    print(titleOfList)
    print("="*35)
    
    # Search Name    
    resultList = [x for x in range(len(arr1)) if arr1[x].upper() == searchText]    
    
    # Display the search result
    for index in resultList:
        print(f"{arr1[index].ljust(30)}{arr2[index]:5n}")        
    
    # If didn;t found display player not found 
    if not resultList:
        print("Name not found!")


def search_player(arr1, arr2):
    # Set a Loop to repeatedly ask the player last name
    ans = input("\nEnter the player last name (0 to Exit) : ")
    
    while ans != "0":                
        search_name(ans, arr1, arr2, f"\n{"Last Name".ljust(30," ")}{"Score".rjust(5," ")}")
        ans = input("\nEnter the player last name (0 to Exit) : ")

    
    
def main():
    # Load data for text file
    playerNameList, battingAvgList = load_data()
    
    # Display the players list
    print_parallel(playerNameList, battingAvgList,f"Player List \n{"Last Name".ljust(30," ")}{"Score".rjust(5," ")}")
    
    # Load Search Player
    search_player(playerNameList, battingAvgList )

main()