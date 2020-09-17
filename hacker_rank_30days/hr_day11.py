# Context: Given a 6 x 6 2D array, A:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

# We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:
# a b c
#   d
# e f g
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

# Task: Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

# Input Format: There 6 lines of input, where each line contains 6 space-seperated integers describing 2D Array A; every value in A will be in 
# the inclusive range of -9 to 9.
# Constraints: -9 <= A[i][j] <= 9, 0 <= i,j <= 5
# Output Format: Print the largest (maximum) hourglass sum found in A.

# Sample Input:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

# Sample Output: 19

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
max = -64
for i in range(0,4):
    for j in range(0,4):
        newmax = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
        max = newmax if max < newmax else max
print(max)
