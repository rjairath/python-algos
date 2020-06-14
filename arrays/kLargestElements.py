# given an array and a number k, print the largest k elements

def kLargest1(arr, k):
    # bubble sort k times and print the last k elements
    n = len(arr)
    for i in range(k):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    for i in range(n-1, n-k-1, -1):
        print(arr[i])


def kLargest2(arr, k):
    arr.sort(reverse=True)

    for i in range(k):
        print(arr[i], end=" ")

    print()


def percDown(arr, i, currentSize):
    while(2*i <= currentSize):
        maxChild = findMaxChild(arr, i, currentSize)

        if arr[i] < arr[maxChild]:
            arr[i], arr[maxChild] = arr[maxChild], arr[i]

        i = maxChild


def findMaxChild(arr, i, currentSize):
    # returns the index of maxChild
    if 2*i + 1 > currentSize:
        return 2*i
    if arr[2*i] > arr[2*i + 1]:
        return 2*i
    else:
        return 2*i + 1


def buildmaxHeap(arr):
    currentSize = len(arr)
    arr = [0] + arr

    i = currentSize // 2
    while(i > 0):
        percDown(arr, i, currentSize)
        i = i//2
    return arr[1:]


def extractLargest(arr):
    currentSize = len(arr)
    arr = [0] + arr

    largest = arr[1]
    arr[1] = arr[currentSize]
    arr.pop()
    currentSize -= 1

    percDown(arr, 1, currentSize)

    return largest, arr[1:]


def kLargest3(arr, k):
    # using maxHeap
    arrNew = buildmaxHeap(arr)
    print(arrNew)
    for i in range(k):
        largest, arrNew = extractLargest(arrNew)
        print(largest)
        # print('arrNew...', arrNew)


    # driver code
if __name__ == '__main__':
    arr = [1, 23, 12, 9, 30, 2, 50]
    kLargest3(arr, 3)
