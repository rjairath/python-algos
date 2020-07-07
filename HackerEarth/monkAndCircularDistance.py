import math


def findPosition(arr, item, start, end):
    while(start < end):
        mid = (start + end) // 2
        if arr[mid] <= item:
            start = mid + 1
        else:
            end = mid

    return start


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        value = input().split()
        x, y = value
        x, y = int(x), int(y)
        # arr.append([x, y])
        d = math.sqrt(x**2 + y**2)
        arr.append(math.ceil(d))

    arr = sorted(arr)
    q = int(input())

    for i in range(q):
        r = int(input())
        temp = findPosition(arr, r, 0, n)
        print(temp)
