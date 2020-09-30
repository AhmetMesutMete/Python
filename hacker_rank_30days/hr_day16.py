# Exceptions - String to Integer

# Task: Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.

# Input Format: A single line string, S.

# Constraints: 1 <= |S| <= 6, where |S| is the length of string S. S is composed of either lowercase letters (a-z) or decimal digits (0-9).

# Output Format: Print the parsed integer value of S, or Bad String if S cannot be converted to an integer.
import sys
try:
    S = input().strip()    
    print(int(S))
except:
    print("Bad String")