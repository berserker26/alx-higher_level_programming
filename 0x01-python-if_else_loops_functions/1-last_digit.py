#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = (-1 * number) % 10
    last_digit *= -1
else:
    last_digit = number % 10
print(f"Last digit of {number:d}", end=' ')
if last_digit > 5:
    print(f"is {last_digit:d} and is greater than 5")
elif last_digit < 5:
    print(f"is {last_digit:d} and is less than 6 and not 0")
else:
    print(f"is 0 and is 0")
