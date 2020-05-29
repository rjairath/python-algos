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


def subArrayRecursive(arr, start, end):
    if end == len(arr):
        return
    if start > end:
        subArrayRecursive(arr, 0, end+1)
    else:
        print(arr[start: end+1])
        subArrayRecursive(arr, start+1, end)


def printSubsequences(arr, index, subarray):
    if index == len(arr):
        # only print non empty subsequence
        print(subarray)
        return

    printSubsequences(arr, index+1, subarray)
    printSubsequences(arr, index+1, subarray+[arr[index]])
    return


arr = [1, 2, 3]
n = len(arr)
subArrayRecursive(arr, 0, 0)
