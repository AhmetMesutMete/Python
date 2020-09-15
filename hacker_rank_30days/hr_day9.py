# Recursion
# Task:
# Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial).

# Input Format:   A single integer, N (the argument to pass to factorial)

# Constraints:    2 <= N <= 12, your submission must contain a recursive function named factorial.

# Output Format: Print a single integer denoting N!.

# Sample Input: 3

# Sample Output: 6

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Number must be an integer")
    if not (n >= 2 or n <= 12):
        raise ValueError("Number must be between 2-12")
    def inner_factorial(n):
        if n <= 1:
            return 1
        return n * inner_factorial(n-1)
    return inner_factorial(n)
n = int(input())
result = factorial(n)
print(result)