def goldMine(mat, row, col, m, n):
    if row < 0 or row >= m:
        return 0
    if col == m-1:
        return mat[row][col]

    return mat[row][col] + max(goldMine(mat, row, col+1, m, n), goldMine(mat, row+1, col+1, m, n), goldMine(mat, row-1, col+1, m, n))

# Now using DP


def goldMineDP(gold, m, n):
    goldTable = [[0 for i in range(n)] for j in range(m)]

    for col in range(n-1, -1, -1):
        for row in range(m):
            # Gold collected on going to
            # the cell on the rigth(->)
            if col == n-1:
                right = 0
            else:
                right = goldTable[row][col+1]

            # Gold collected on going to
            # the cell to right up (/)
            if row == 0 or col == n-1:
                right_up = 0
            else:
                # print('right_up', right_up)
                right_up = goldTable[row-1][col+1]

            # Gold collected on going to
            # the cell to right down (\)
            if row == m-1 or col == n-1:
                right_down = 0
            else:
                # print("right_down", right_down)
                right_down = goldTable[row+1][col+1]

            # defined 3 paths above
            goldTable[row][col] = gold[row][col] + \
                max(right, right_up, right_down)

    res = goldTable[0][0]
    for i in range(m):
        res = max(res, goldTable[i][0])

    return res


gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]

m = 4
n = 4

maxValue = 0
# for i in range(m):
#     x = goldMine(gold, i, 0, m, n)
#     if x > maxValue:
#         maxValue = x

# print(maxValue)

x = goldMineDP(gold, m, n)
print(x)
