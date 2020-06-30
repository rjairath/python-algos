# arr here is a 2d array

def inversion(mat, val, row, col, n):
    count_item = 0
    for i in range(row, n):
        for j in range(col, n):
            if mat[i][j] < val:
                count_item += 1

    return count_item


def countInversions(mat, n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += inversion(mat, mat[i][j], i, j, n)

    return count


if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())
        mat = []
        for j in range(n):
            mat.append([int(j) for j in input().split()])

        # print(mat)

        count = countInversions(mat, n)
        print(count)
