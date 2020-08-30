# Task:
#     Given a string, S, of length N that is indexed from 0 to N - 1, print its even-indexed and odd indexed characters as 2 space-seperated
# strings on a single line.
# Note: 0 is considered to be an even index.
# Input Format:
# The first line contains an integer, T (the number of test cases).
# Each line i of the T subsequent lines contain a String, S.
# Constraints: 1 <= T <= 10, 2 <= length of S <= 10000

# Output Format:
# For each String Sj (where 0 <= j <= T - 1), print Sj's even-indexed characters, followed by a space, followed by Sj's odd-indexed characters.

# Sample Input: 
# 2
# Hacker
# Rank

# Sample Output:
# Hce akr
# Rn ak
T = int(input())    # Number of test cases
if 1 <= T and T <= 10:
    pass
else:
    raise Exception("Request denied. Out of bounds") 
for i in range(T):
    ex = input()  
    if 2 <= len(ex) and len(ex) <= 10000:
        pass
    else:
        raise Exception("String length is out of bounds")
    evenchr = ""
    oddchr = ""
    for i in range(len(ex)):
        if i % 2 == 0:
            evenchr += ex[i]
        else:
            oddchr += ex[i]
    print(f"{evenchr} {oddchr}")