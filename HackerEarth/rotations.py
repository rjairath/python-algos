def rotateArray(arr, k):
    n = len(arr)
    k = k % n
    arr2 = [0 for i in range(n)]

    j = 0
    for i in range(n-k, n):
        arr2[j] = arr[i]
        j += 1

    for i in range(n-k):
        arr2[j] = arr[i]
        j += 1

    return arr2


# arr = [1, 2, 3, 4, 5]
# k = 2
# arr2 = rotateArray(arr, k)
# print(arr2)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        value = input()
        n, k = value.split()
        n, k = int(n), int(k)

        arr = [int(j) for j in input().split()]
        arr2 = rotateArray(arr, k)
        print(arr2)
