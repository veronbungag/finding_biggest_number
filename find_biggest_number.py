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
#else 
#if second number is greater than third number
#else third number is biggest number