############### Part 1
# def greeting(name):
#     print('Hello ', name)

# # print(greeting('Mesut')) 
# # print(greeting)        #It'll tell that there is a definition of object for greeting. Type of greeting is function and it has an adress in memory

# sayHello = greeting     #In here we assigned greeting object to another variable. Actually we didn't assign the content. We assigned the address of content to another variable

# print(sayHello)         #It'll give the exact same adress with greeting object. Also we can use it as same as greeting function now => sayHello(name)
# print(greeting)

# print(sayHello("my dear friend"))

# del sayHello            #If we delete the sayHello we'll just erase the definition of sayHello, not the content inside that adress.
# print(greeting)

############################################ Part 2
# Encapsulation
# def outer(num1):
#     print('outer')
#     def inner_increment(num1):
#         print('inner')
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1, num2)


# outer(10)
# inner_increment(10) #It'll give NameError

############################################# Part 3
def factorial(number):
    if not isinstance(number, int):    # The isistance() function returns True if the specified object is of the specified type, otherwise False.
        raise TypeError("Number must be an integer")

    if not number >= 0:
        raise ValueError("Number must be greater or equal to 0")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

# manner of work => 5*in(4) = 5*4*in(3) = 5*4*3*in(2) = 5*4*3*2*in(1) = 5*4*3*2*1 = 120

try:
    print(factorial('a'))
except Exception as ex:
    print(ex)
