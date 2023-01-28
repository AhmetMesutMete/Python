import sys

'''
Print the sum of even fibonacci numbers below given number
'''

# First line denotes the number of test cases

# Each of the following line contains an integer, N. 

def fib(n, memo={}):
    if n in memo: return memo[n]
    if n <= 2:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

    
t = int(input('Please indicate the number of test cases: ').strip())
for _ in range(t):
    n = int(input('Please type a positive integer between 10 and 4*(10**16): ').strip())
    k = 1
    a, res = 0 , 0  
    while True:
        a = fib(k)
        if a < n:
            if a % 2 == 0:
                res += a
        else:
            break
        k += 1
    print(res)