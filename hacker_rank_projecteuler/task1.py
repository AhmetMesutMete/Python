# For each test case, print an integer that denotes the sum of all the multiples of 3 or 5 below N.

# First line denotes the number of test cases

# Each of the following line contains an integer, N. 
      
t = int(input('Please indicate the number of test cases: ').strip())
for _ in range(t):
    n = int(input('Please type a positive integer below 10**9 + 1:').strip()) - 1
    res = 3*(n//3)*(n//3+1)//2 + 5*(n//5)*(n//5+1)//2 - 15*(n//15)*(n//15+1)//2
    print(int(res))