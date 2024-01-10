#import tkinter interface
from tkinter import *

#define find biggest number
#ask user to input three numbers and store in each variables

def find_biggest():
     first = int(first.get())
     second = int(second.get())
     third = int(third.get())
 
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
     result_label.config(text="The biggest number is: " + str(biggest))
            

find_biggest()

#create a window root with title "Find biggest number"
root = Tk()
root.title("Biggest Number Finder")
root.geometry("900x300")
root.config(background = "pink") 

frame = Frame(root)
frame.pack()
#Display a dialog box asking the user to enter the first number
first_number = Label(frame, text="Enter first number:", font="Courier", bg="pink")
first_number.pack(side=LEFT)
first_number = Entry(frame)
first_number.pack(side=LEFT)
#Display a dialog box asking the user to enter the second number
#Display a dialog box asking the user to enter the third number
#add button
#Display a dialog box showing the result
