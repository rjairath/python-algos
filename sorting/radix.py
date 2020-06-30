# exp here is the place to sirt...1s, 10s, 100s
def countingSort(arr, exp):
    n = len(arr)
    output = [0]*n
    count = [0]*10

    # update the count array
    for i in range(n):
        index = arr[i]//exp
        count[index % 10] += 1

    # print(count, 'count..', exp)
    # cumulative
    for i in range(1, 10):
        count[i] += count[i-1]

    # now compare the original array
    i = n-1
    while i >= 0:
        index = (arr[i]//exp)
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix(arr):
    max1 = max(arr)

    exp = 1

    while max1/exp > 1:
        countingSort(arr, exp)
        exp *= 10


arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix(arr)
print(arr)
