"""
Charlotte Wilson
cwil323
8786167
Assignment 1 Question 4
"""
import random

print("*" * len("  University of Auckland Username Generator  "))
print("  University of Auckland Username Generator  ")
print("*" * len("  University of Auckland Username Generator  "))
print()
student_name = input("Please enter your name: ")
student_name = student_name.strip()

first_space = student_name.find(" ")
first_name = student_name[0:1]
first_name = first_name.strip()
last_name = student_name[first_space + 1:]
last_name = last_name.strip()
username = first_name + last_name
username = username[0:4]

random_number = random.randrange(1,1000)
random_number = str(random_number)
username_number = "00" + random_number 
username_number = username_number[-3:]
full_username = username + username_number
full_username = full_username.lower()

print()     
print("Your username is", full_username)
