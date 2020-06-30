def findNiceStrings(arr):
    temp = [0 for i in range(len(arr))]

    for i in range(1, n):
        count = 0
        for j in range(0, i):
            if arr[j] < arr[i]:
                count += 1

        temp[i] = count

    for k in range(len(temp)):
        print(temp[k], end=" ")
    print()


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())

    findNiceStrings(arr)
