'''
    Find the largest prime factor of a given number

    Ex: Prime factors of 10 is 2 and 5 so the largest prime factor of 10 is 5.
'''

# First line denotes the number of test cases

# Each of the following line contains an integer, N. 

T = int(input())
for _ in range(T):
    N = int(input())
    i = 2
    largest_prime = 2
    while i*i <= N:
        while N % i == 0:
            largest_prime = i
            N //= i    
        i += 1
    if N>largest_prime:
        largest_prime = N;
    print(largest_prime)