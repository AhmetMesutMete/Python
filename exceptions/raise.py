x = 10
if x > 5:
    raise Exception("x can not be greater than 5.")


########################

# def check_password(psw):
#     import re               # regular expressions library
#     if len(psw) < 8:
#         raise Exception("Password must contain at least 8 characters")
#     elif not re.search("[a-z]",psw):
#         raise Exception("Password must contain lowercase")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("Password must contain uppercase")
#     elif not re.search("[0-9]",psw):
#         raise Exception("Password must contain numbers")
#     elif not re.search("[_@$]",psw):
#         raise Exception("Password must contain alpha numeric characters")
#     elif not re.search("[\s]",psw):             # \s stands for space character
#         raise Exception("Password mustn't contain spaces")
#     else:
#         print("Valid Password")

# password = "12345687aA@ "

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("Valid Password")
# finally:
#     print("Validation completed.")

# class Person:
#     def __init__(self, name, year):
#         if len(name) > 10:
#             raise Exception("Name can not contain more than 10 characters")
#         else:
#             self.name = name

# p = Person("Cancacnacancanac", 1999)