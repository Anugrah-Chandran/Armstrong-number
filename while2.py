'''Author: Anugrah Chandran
Date: 25-10-24
Description: Python program to find whether the number is an Armstrong number
'''
number=int(input("Enter your number:"))
sum_of_digits = 0
while number>0:
    number = number%10
    remainder = number**3
    number = number//10
if sum_of_digits == number:
    print("Given number is an Armstrong number")
else:
    print("Given number is not an Armstrong number ")

