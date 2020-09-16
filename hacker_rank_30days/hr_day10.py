# Task:
# Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 
# 1's in n's binary representation.

# Input Format: A single integer, n.

# Constraints: 1 <= n <= 10**6

# Output Format: Print a single base-10 integer denoting the max. number of consecutive 1's in binary representation of n.

# Sample Input 1: 1
# Sample Output 1: 1

# Sample Input 2: 13
# Sample Output 2: 2

n = int(input())
def dec_to_bin(n):
    result = ''
    while True:
        if n % 2 == 1:
            result = '1' + result
        elif n == 0:
            return result
        else:
            result = '0' + result
        n = int(n / 2)
    return result
a = dec_to_bin(n).split('0')
b = [len(a[i]) for i in range(len(a))]
b.sort()
print(b[-1])


