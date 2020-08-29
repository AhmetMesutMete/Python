# Generators: If it is not necessary to store a value that you create and if you'll only use it at the moment and won't need it in the future
# def cube():
#     for i in range(5):
#         yield i ** 3 

# for i in cube():
#     print(i)
list1 = (i ** 3 for i in range(10))

print(list1)
while True:
    try:
        element = next(list1)
        print(element)
    except StopIteration:
        break