#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:10:14 2026

@author: flkc
Description:
    Watch the video on creating a simple class. Create the class in the video and test it to make sure
it works.
Add a method to the class that accepts a bonus rate for the employee. It should then compute
the employee bonus of rate x salary and return this value. Demonstrate this method works by
entering a bonus rate and displaying the bonus.
"""

class Employee:
    employeeID = ""
    firstName = ""
    lastName = ""
    address = ""
    city = ""
    state = ""
    zipCode = ""
    salary = 0.0
    bonuseRate = 0.0
    
    def __init__(self,employeeID,firstName,lastName):
        self.employeeID = employeeID
        self.firstName = firstName
        self.lastName = lastName
        self.name = self.fullName()
    
    def acceptBonusRate(self):        
        self.bonusRate = float(input(f"{"Enter the bouns rate: ".ljust(30," ")}"))
        return self.bonusRate * self.salary
    
    def fullName (self):        
        self.name =  self.firstName + " " + self.lastName
        return self.name
    
        


def main():
    employee1 = Employee("E00001", "Peter", "Chan")
    employee1.address = "1234 W Golf Rd."
    employee1.city = "Schaumburg"
    employee1.state = "IL"
    employee1.zipCode = "60173"
    employee1.salary  = 7000
    
    print (f"{"Name:".ljust(30," ")}{employee1.name}\n{"Address:".ljust(30," ")}{employee1.address}, {employee1.city}, {employee1.state}, {employee1.zipCode}\n{"Salary:".ljust(30," ")}{employee1.salary:,}")
    
    
    print( f"{"Bonus:".ljust(30," ")}{employee1.acceptBonusRate():,.2f}")
    
    
        
main()