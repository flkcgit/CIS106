# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:47:56 2026

@author: flkc
Description:
    Create a student class. This class should consist of student first name, student last name, district
code (I or O) and enrolled credits. Create a method to compute tuition owed. Tuition owed
should be enrolled credits times $250.00 per credit hour for in district students (district code of
I) and or times $500.00 per credit hour for out of district students (district code of anything
other than I). Test the class by instantiating the object and adding data
"""

class Student:
    firstName = ""
    lastName = ""
    districtCode = ""
    enrolledCredit = 0
    TUITION_PER_HOUR = {"I":250,
                       "O":500}
    
    def __init__(self,firstName,lastName,districtCode = "O",enrolledCredit = 0):
        self.firstName = firstName
        self.lastName = lastName
        self.districtCode = districtCode
        self.enrolledCredit = enrolledCredit
        self.name = self.fullName()
    
    def computeTuition (self):
        
        if self.districtCode.upper() == "I":
            return self.enrolledCredit * self.TUITION_PER_HOUR["I"]
        else:
            return self.enrolledCredit * self.TUITION_PER_HOUR["O"]
        
    def fullName (self):
        return self.firstName + " " + self.lastName
    
    def printStudent(self):
        print(f"\n{"Student Name:".ljust(30," ")}{self.name}")
        print(f"{"District Code:".ljust(30," ")}{self.districtCode}")        
        print(f"{"Enrolled Credit:".ljust(30," ")}{self.enrolledCredit}")
        print(f"{"Tuition Owed:".ljust(30," ")}{self.computeTuition()}\n")
        
def main():
    # Create an instance of Student
    student1 = Student("Patrick", 
                       "Chan", 
                       "I",
                       12)
    student2 = Student("Johnson",
                       "Wong",
                       "O",
                       12)
    
    
    student1.printStudent()
    student2.printStudent()
    
main()