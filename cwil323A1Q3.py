"""
Charlotte Wilson
cwil323
8786167
Assignment 1 Question 3
"""

number1 = int(input("Please enter the first integer: "))
number2 = int(input("Please enter the second integer: "))
number3 = int(input("Please enter the third integer: "))
number4 = int(input("Please enter the fourth integer: "))

min_number = min(number1, number2, number3, number4)
max_number = max(number1, number2, number3, number4)
small_mid_number = max(min(number1, number2, number3), min(number1, number3, number4), \
                     min(number1, number2, number4), min(number2, number3, number4))
big_mid_number = min(max(number1, number2, number3), max(number1, number3, number4), \
                       max(number1, number2, number4), max(number2, number3, number4))
print()
print("The integers in increasing order of size are: ", min_number, ", ", small_mid_number, ", ", big_mid_number, ", and ", max_number, sep = "")
