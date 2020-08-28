####################### Part 1
# def base(number):

#     def inner(power):
#         return number ** power

#     return inner

# two = base(2)
# three = base(3)

# print(two(5))
# print(three(4))

####################### Part 2
# def check_authorization(page):

#     def inner(role):
#         if role == 'Admin':
#             return "{0} has access to {1}.".format(role, page)
#         else:
#             return "{0} has no access to {1}".format(role, page)
#     return inner

# user1 = check_authorization("Product Edit Page")
# print(user1('Admin'))
# print(user1("User"))

######################## Part 3

def operation(OpName):
    if not (OpName == "sum" or OpName == "mul"):
        raise Exception("There are only two operations in this function; sum and mul. ")

    def sum(*args):
        for j in args:
            if not isinstance(j, int):
                raise ValueError("Argument type must be integer")  
        sum = 0
        for i in args:
            sum += i
        return sum
    
    def mul(*args):
        for i in args:
            if not isinstance(i, int):
                raise ValueError("Argument type must be integer")  
        mul = 1
        for j in args:
            mul *= j
        return mul

    if OpName == "sum":
        return sum
    else: 
        return mul
try:
    sum1 = operation("sum")
    print(sum1(1,'2',3,4,132,421))
    
except Exception as ex:
    print(ex)

mul1 = operation("mul")
print(mul1(3,4,6,8))