#import tkinter interface
import tkinter as tk
from tkinter import messagebox

#define find biggest number
#ask user to input three numbers and store in each variables

def find_biggest():
 first = int(input("Enter first number:"))
 second = int(input("Enter second number:"))
 third = int(input("Enter third number:"))
 
 #if first number is greater than second number
 if first > second:
      #if first number is greater than third number
        if first > third:
            biggest = first
      #else store third number is biggest number
        else:
            biggest = third
 else:
      #if second number is greater than third number
        if second > third:
            biggest = second
      #else third number is biggest number
        else:
            biggest = third 
 #print data
 print("The biggest number is: ", biggest)

find_biggest()

#create a window root with title "Find biggest number"
root = tk.Tk()
root.title("Biggest Number Finder")
root.geometry("900x300")
root.config(background = "pink") 

frame = Frame(root)
frame.pack()
#Display a dialog box asking the user to enter the first number

#Display a dialog box asking the user to enter the second number
#Display a dialog box asking the user to enter the third number
#add button
#Display a dialog box showing the result
