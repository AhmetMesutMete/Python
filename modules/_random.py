import random

# result = dir(random)
# result = help(random)

result = random.random()                            # Produces a number between 0.0 - 1.0
result = random.random() * 100      
result = random.uniform(1,10)                       # Produces a number between 1-10
result = int(random.uniform(1,10))                  # Produces an integer number between 1-10
result = random.randint(1,100)                      # Produces an integer number between 1-100 by using randint(from x, till y)

names = ['Sam', 'Gregor', 'Tom', 'Danny']

result = names[random.randint(0, len(names) - 1)]
result = random.choice(names)                       # random.choice helps us to choose one member of a given list randomly

greeting= 'hello there'
result = random.choice(greeting) 

list1 = list(range(10))
random.shuffle(list1)                               

result = list1


list2 = range(100)
result = random.sample(list2, 3) # random.sample takes requested number of random sample from a given list 
result = random.sample(names, 2)

print(result)