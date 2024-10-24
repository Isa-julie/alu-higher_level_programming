#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)  # Random signed number

# Get the last digit
last_digit = abs(number) % 10  # Use abs to ensure the last digit is positive

# Prepare the output
print(f"Last digit of {number} is {last_digit}", end=" ")

# Check conditions for the last digit
if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:  # last_digit < 6
    print("and is less than 6 and not 0")
