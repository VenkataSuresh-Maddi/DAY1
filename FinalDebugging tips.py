#DESCEIBING THE PROBLEM
def my_function():
    for i in range(1, 20):  # Looping from 1 to 19 (range is exclusive of 20)
        if i == 20:  # This condition will never be met, because the loop stops at 19
            print("You got it")


my_function()

# 1. What is the for loop doing?
#    - It loops from 1 to 19, incrementing `i` by 1 in each iteration.
# 
# 2. When is the function meant to print "You got it"?
#    - It is supposed to print "You got it" when `i` equals 20.
#
# 3. What are your assumptions about the value of i?
#    - The assumption might be that `i` would reach 20, but `range(1, 20)` only goes up to 19.
#
# 🔧 FIX:
#    - Change `range(1, 21)` so that `i` reaches 20.



#REPRODUCE THE BUG
from random import randint

dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)  # randint(1, 6) returns values between 1 and 6

print(dice_num)  # Debug print to see what number is generated
print(dice_images[dice_num - 1])  # Fix: Use `dice_num - 1` because list indexing starts from 0

#PLAY COMPUTER
year = int(input("What's your year of birth? "))

if 1980 <= year <= 1994:  # Fix: Include 1980 in millennial range
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
else:
    print("You are from a different generation.")  # Added case for years before 1980


#FIX THE ERRORS
try:
    age = int(input("How old are you? "))
    if age > 18:
        print(f"You can drive at age {age}.")
    else:
        print(f"You're too young to drive at age {age}.")
except ValueError:  # Handles invalid input (e.g., letters instead of numbers)
    print("You have entered an invalid number. Please enter a numeric value.")




#USE PRINT
pages = int(input("Number of pages: "))
words_per_page = int(input("Number of words per page: "))

total_words = pages * words_per_page

# Debug prints
print(f"pages = {pages}")
print(f"words_per_page = {words_per_page}")
print(f"Total words = {total_words}")  # Fix: Improved print formatting



#USE A DEBUGGER
def add(n1, n2):
    """Returns the sum of two numbers"""
    return n1 + n2

import random  # Fixed import
import math  # Fix: Changed from "maths" to "math" (correct library name)

def mutate(a_list):
    """Mutates a list by doubling each number, adding a random offset, and summing with the original."""
    b_list = []
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = add(new_item, item)  # Fix: Used the correct 'add' function
        b_list.append(new_item)

    print(b_list)  # Debug output to verify the result

mutate([1, 2, 3, 5, 8, 13])
