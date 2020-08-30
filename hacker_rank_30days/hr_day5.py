# Task:
#     Given an integer, n, print its first 10 multiples. Each multiple n x i (where 1 <= i <= 10) 
# should be printed on a new line in the form: n x i = result.
# Input Format: A single integer
# Constraints: 2 <= n <= 20
# Output Format:
# Print 10 lines of output: each line i(where 1 <= i <= 10) contains the result of n x i in the form: n x i = result.
# Sample Input: 2
# Sample Output:
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20
import math
import os
import random
import re
import sys

# n = int(input())
# if n >= 2 and n <= 20:
#     list1 = [n*i for i in range(1,11)]
#     for i in range(10):
#         print(f"{n} x {i+1} = {list1[i]}")
# else:
#     raise Exception("Out of bounds")

n = int(input())
try:
    if n >= 2 and n <= 20:
        list1 = [n*i for i in range(1,11)]
        for i in range(10):
            print(f"{n} x {i+1} = {list1[i]}")
    else:
        raise Exception("Out of bounds")
except Exception as ex:
    print(ex)