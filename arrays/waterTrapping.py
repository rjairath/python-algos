def calculateHeight(arr):
    l = 0
    r = len(arr)-1
    sum = 0
    for i in range(l+1, r):
        a = 0
        b = 0
        for j in range(l, i+1):
            if arr[j] > a:
                a = arr[j]
        for k in range(i, r+1):
            if arr[k] > b:
                b = arr[k]

        sum += min(a, b) - arr[i]

    return sum


def calculateHeight2(arr):
    n = len(arr)

    left = [0]*n
    right = [0]*n

    _max = -1
    sum = 0

    for i in range(0, n):
        if arr[i] > _max:
            _max = arr[i]
        left[i] = _max

    _max = -1
    for j in range(n-1, 0, -1):
        if arr[j] > _max:
            _max = arr[j]
        right[j] = _max

    for k in range(1, n-1):
        sum += min(left[k], right[k]) - arr[k]
    return sum


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
ans = calculateHeight2(arr)
print(ans)
