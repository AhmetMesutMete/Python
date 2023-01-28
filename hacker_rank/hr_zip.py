"""
Task

The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.
Sample Input

5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

Sample Output

90.0 
91.0 
82.0 
90.0 
85.5     
"""
N, X = input().split()
s = [0, 0, 0]
sum = 0
for i in range(int(X)):
    s[i] = input().split()
k = zip(s[0], s[1], s[2])
for i in k:
    sum = float(i[0]) + float(i[1]) + float(i[2])
    print(sum/3)

n, x = map(int, input().split()) 

sheet = []
for _ in range(x):
    sheet.append( map(float, input().split()) ) 

for i in zip(*sheet): 
    print( sum(i)/len(i) )