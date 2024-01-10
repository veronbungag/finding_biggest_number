#import tkinter interface
from tkinter import *

#define find biggest number
#ask user to input three numbers and store in each variables

def find_biggest():
     first = int(first_number.get())
     second = int(second_number.get())
     third = int(third_number.get())
 
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
second_number = Label(frame, text="Enter second number:", font="Courier", bg="pink")
second_number.pack(side=LEFT)
second_number = Entry(frame)
second_number.pack(side=LEFT)
#Display a dialog box asking the user to enter the third number
third_number = Label(frame, text="Enter third number:", font="Courier", bg="pink")
third_number.pack(side=LEFT)
third_number = Entry(frame)
third_number.pack(side=LEFT)
#add button
button = Button(root, text="Find Biggest", command=find_biggest, font="Courier", bg="pink")
button.pack()
#Display a dialog box showing the result
result_label = Label(root, text="The biggest number:", font="Courier", bg="pink")
result_label.pack()

root.mainloop()