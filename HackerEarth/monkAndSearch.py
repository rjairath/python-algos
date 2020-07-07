
def lower_bound(arr, item, start, end):

    while(start < end):
        mid = (start + end) // 2
        if arr[mid] >= item:
            end = mid
        else:
            start = mid + 1

    return start


def upper_bound(arr, item, start, end):

    while(start < end):
        mid = (start + end) // 2

        if arr[mid] <= item:
            start = mid + 1
        else:
            end = mid

    return start


def computeValues(arr, x, item):
    n = len(arr)
    if x:
        print(n - upper_bound(arr, item, 0, n))

    else:
        print(n - lower_bound(arr, item, 0, n))


if __name__ == "__main__":
    n = int(input())
    arr = [int(j) for j in input().split()]
    arr = sorted(arr)
    # sorting in o(nlogn)
    q = int(input())
    for i in range(q):
        values = input().split()
        x, y = values
        x, y = int(x), int(y)
        computeValues(arr, x, y)
