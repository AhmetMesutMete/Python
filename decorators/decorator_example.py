# Decorator functions used to add a new feature to a function
# def my_decorator(func):
#     def wrapper(name):
#         print("operations before func.")
#         func(name)
#         print("operations after func.")
#     return wrapper

# @my_decorator
# def sayHello(name): # If we want to add parameter to sayHello func. than also we should add the same parameter to wrapper() and func() as well
#     print("Hey there, I am", name)

# # sayHello = my_decorator(sayHello) # or @my_decorator
# sayHello("Chris")

################## Another Example
import math
import time

def calc_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print(func.__name__ + " function run time is "+ str(finish - start))
    return inner

@calc_time
def TakePower(a,b):
    print(f"{a} to the power of {b} is equal to",math.pow(a,b))
    
@calc_time
def factorial(number):
    print(f"The factorial of {number} is equal to",math.factorial(number))
    

TakePower(5,3)
factorial(6)