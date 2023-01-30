import numpy as np

# First line denotes the number of spirals that are gonna be created

# Each of the following line contains two space-seperated integers indicating row and column values accordingly.
def create_spiral(row, col):
    '''
        This function generates a spiral based on the row and column values specified.
        Starting in the upper left corner of the array, increasing numbers are written to the right,
        down, left, up, and so on until they reach the end point and form a spiral.
    '''
    arr = np.ones((row, col)).astype(int)
    right = col - 1
    left = 0
    top = 0
    bottom = row - 1
    count = 1
    while True:
        if left > right:
            break
        # prtop row
        for i in range(left, right + 1):
            arr[top][i] = count
            count += 1
        top += 1

        if top > bottom:
            break

        # prright column
        for i in range(top, bottom + 1):
            arr[i][right] = count
            count += 1
        right -= 1

        if left > right:
            break

        # prbottom row
        for i in range(right, left - 1, -1):
            arr[bottom][i] = count
            count += 1
        bottom -= 1

        if top > bottom:
            break

        # prleft column
        for i in range(bottom, top - 1, -1):
            arr[i][left] = count
            count += 1
        left += 1
    # print(arr)
    for i in range(row):
        for j in range(col):
            print(arr[i][j],end= " ")
        print()


T = int(input())

for _ in range(T):
    r, c = map(int, input().split())
    create_spiral(r, c)
