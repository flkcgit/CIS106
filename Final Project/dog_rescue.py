# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:14:28 2026

@author: flkc
"""

MENU_ITEM=["Add a Dog","View Dogs","Find Dog","Quit"]
dogs = []




class Dog:
    name = ""
    breed = ""
    age = 0
    weight = 0
    
    def __init__(self,name,breed,age,weight):
        self.name = name
        self.breed = breed
        self.age = age
        self.weight = weight
        
    # def printDog(self):        
    #     print(f"\n{"Dog Name:".ljust(30," ")}{self.name}")
    #     print(f"{"Dog Breed:".ljust(30," ")}{self.breed}")        
    #     print(f"{"Age:".ljust(30," ")}{self.age}")
    #     print(f"{"Weight:".ljust(30," ")}{self.weight}\n")


def menu():
    #print("\n"*100)    
    print("\nDog Rescue")
    print("-------------")
    for x in range(len(MENU_ITEM)):
        print(f"{x+1}. {MENU_ITEM[x]}")
    return input("\n\nSelect a choice: ")

    
def addDog():
    
    # Enter Dog information
    print("\nEnter the dog information\n")
    name = input(f"{"Dog Name:".ljust(30," ")}")
    breed = input(f"{"Dog Breed:".ljust(30," ")}")
    age = input(f"{"Dog Age:".ljust(30," ")}")
    weight = input(f"{"Dog Weight:".ljust(30," ")}")
    
    # create an instance for dog and append to dogs list
    dogs.append(Dog(name,breed,age,weight))
    
    print(f"\n{name} added.")
    
    
def viewDogs():
    # Print the title of table
    print("\nRescue Dogs")
    print("-"*65)
    print(f"{"Dog".ljust(15," ")}{"Breed".ljust(30," ")}{"Age".rjust(10," ")}{"Weight".rjust(10," ")}")
    print("-"*65)
    
    # Loop and print the dogs list
    for x in dogs:
        print(f"{x.name.ljust(15," ")}{x.breed.ljust(30," ")}{x.age.rjust(10," ")}{x.weight.rjust(10," ")}")
    
def findDog():
    # Set isNotFound = True as default
    isNotFound = True
    
    # Enter the dog name
    searchName = input("\nEnter dog name to search: ")
    
    # Loop the dogs list to search
    for x in dogs:
        
        # If found, display the name, and set isNotFound = False
        if x.name.upper() == searchName.upper():
            print (f"\nFound {x.name}\n")
            isNotFound = False
            break
    
    # After the Loop, if not found, print the not found message
    if isNotFound:
        print(f"\nSorry, unable to find {searchName}\n")
        
    
def main():
    ans = menu()    
    while ans != "4":        
        if ans == "1":
            addDog()
        elif ans =="2":    
            viewDogs()
        elif ans == "3":
            findDog()
        input("\nPress any key to continue     ")
        ans = menu()        
        
    else:
        print("Good bye")
        
    
    
    
main()