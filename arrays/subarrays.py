# subarray iterative
# print all subarrays
def subArray(arr):
    n = len(arr)
    for i in range(0, n):
        # i is starting point
        for j in range(i, n):
            # j is ending point
            for k in range(i, j+1):
                print(arr[k], end="")
            print()


arr = [1, 2, 3, 4]
subArray(arr)
