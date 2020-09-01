# Task
#     Given an array, A, of N integers, print A's elements in reverse order as a single line of space-seperated numbers.
# Input Format:
# The first line contains an integer, N  (the size of our array)
# The second line contains N space-seperated integers describing array A's elements.

# Constraints:    
# 1 <= N <= 1000
# 1 <= Ai <= 10000, where Ai is the ith integer in the array

# Output Format:
# Print the elements of array A in reverse order as a single line of space-seperated numbers.

# Sample Input:
# 4
# 1 4 3 2

# Sample Output:
# 2 3 4 1
import math
import os
import random
import re
import sys

n = int(input())
if 1 <= n <= 1000:
    pass
else:
    raise Exception("N is out of bounds")
arr = list(map(int, input().rstrip().split()))
for i in range(len(arr)):
    if 1 <= arr[i] <= 10000:
        pass
    else:
        raise Exception("At least an element's value is out of bounds.")
arr.reverse()
k = ""
for i in range(n):
    k += str(arr[i])
    k += " "
print(k)
