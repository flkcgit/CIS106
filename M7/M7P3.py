# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:26:24 2026

@author: flkc
Description: 
    Prompt the user on whether they want to do this program (just before the while loop). “Yes”
entry means they want to continue. Any other response indicates they will stop the program.
This response is the loop control variable. If the user answers “Yes “then go into the while loop.
Note: you may use any variation or yes as shown in class to continue.
Once in the while loop. You are to prompt the user for their last name and two exam scores.
Compute the average exam score. Display last name and average. After the loop, display a count
of the number of students who entered data.
Finally, the last statements within the while loop will ask the user if they want to do this loop
again. In other words, the user needs to be prompted again. The reason is that the end of the
loop takes execution to the while condition to be evaluated again. It cannot take us to the first
few lines of code that prompt the user for the first time. That code is out of the loop. Therefore,
we need a second prompt at the bottom, inside the loop.
"""

noOfStudent = 0
ans = input("Whether want to do this program (Yes/No): ")


while ans == "Yes":
    lastName = input("Enter your last name: ")
    examOneScore = int(input("Enter the exam one score: "))
    examTwoScore = int(input("Enter the exam two score: "))
    averageScore = (examOneScore + examTwoScore) / 2
    print(f"\nLast name:     {lastName}")
    print(f"Average Score: {averageScore:3.2f}")
    print("---------------------------------\n")
    noOfStudent += 1
    ans = input("Whether want to do this program (Yes/No): ")

print(f"Total {noOfStudent:3.0f} students who entered data!")
    
    
    