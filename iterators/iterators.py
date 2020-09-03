list1 = [1, 2, 12, 34, 82]

iterator = iter(list1)

print(next(iterator)) # It'll show the first element of list1 (Next element will be shown at each time)
print(next(iterator)) 
print(next(iterator)) 
print(next(iterator))
print(next(iterator)) 
print(next(iterator)) # It'll give an error because all elements displayed and there is no next element

# for i in list1: # We can display the elements using for loop
#     print(i)

# iterator = iter(list1)

# while True: 
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

# class MyNumbers:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.start <= self.stop:
#             x = self.start
#             self.start += 1
#             return x
#         else:
#             raise StopIteration

# list = MyNumbers(10,40)

# my_iter = iter(list)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# for x in list:
#     print(x)