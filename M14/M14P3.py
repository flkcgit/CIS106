# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:47:56 2026

@author: flkc
Description:
    Modify problem 2 to use a dictionary for the district code pair. Make sure it works. Expand the
dictionary to include X for international students whose tuition is $800.00 per credit hour and G
for reciprocity students whose tuition the same as an I student. instantiate at least one student
of each district code.
Some colleges have reciprocity agreements where a student from another school can take
classes at in district rates. This usually applies to classes not offered by the home college. Harper
does not have a commercial truck driver program for example.
"""

class Student:
    firstName = ""
    lastName = ""
    districtCode = ""
    enrolledCredit = 0
    TUITION_PER_HOUR = {"I":250,
                       "O":500,
                       "X":800,
                       "G":250}
    
    def __init__(self,firstName,lastName,districtCode = "O",enrolledCredit = 0):
        self.firstName = firstName
        self.lastName = lastName
        self.districtCode = districtCode.upper()
        self.enrolledCredit = enrolledCredit
        self.name = self.fullName()
    
    def computeTuition (self):        
        return self.enrolledCredit * self.TUITION_PER_HOUR[self.districtCode]
        
        
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
    student3 = Student("Andy",
                       "Chan",
                       "X",
                       12)
    student4 = Student("Eric",
                       "Tang",
                       "G",
                       12)
    
    
    student1.printStudent()
    student2.printStudent()
    student3.printStudent()
    student4.printStudent()
    
main()