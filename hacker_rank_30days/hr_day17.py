# More Exceptions

# Task: Write a Calculator class with a single method: int power(int,int). The power method takes two integers, n and p, as parameters and returns
# the integer result of n^p, if either n or p is negative, then the method must throw an exception with the message: n and p should be non-negative.

# Input Format: Input from stdin is handled for you by the locked stub code in your editor. The first line contains an integer, T, the number of
# test cases. Each of the T subsequent lines describes a test case in 2 space-seperated integers denoting n and p respectively.

# Constraints: No Test Case will result in overflow for correctly written code.

# Output Format: Output to stdout is handled for you by the locked stub code in your editor. There are T lines of output, where each line 
# contains the result of n^p as calculated by your Calculator class' power method.
class Calculator:
    def power(self,n, p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        return n**p
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)  