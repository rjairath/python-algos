from collections import Counter
remainder = 100000


def sorting(arr, exp):
    output = [0 for i in range(len(arr))]
    frequency = [0 for j in range(remainder)]

    for i in range(len(arr)):
        temp = (arr[i]//exp) % remainder
        frequency[temp] += 1

    for j in range(1, remainder):
        frequency[j] += frequency[j-1]

    # for i in range(len(arr)):
    #     temp = (arr[i]//exp) % remainder
    #     frequency[temp] -= 1
    #     index = frequency[temp]
    #     output[index] = arr[i]

    i = len(arr)-1
    while i >= 0:
        index = (arr[i]//exp)
        output[frequency[(index) % remainder] - 1] = arr[i]
        frequency[(index) % remainder] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]
        print(arr[i], end=" ")
    print()


if __name__ == "__main__":
    # n = int(input())
    # arr = [int(j) for j in input().split()]

    arr = [213456789, 167890, 123456789]
    exp = 1
    max1 = max(arr)
    while(max1//exp > 1):
        sorting(arr, exp)
        exp *= 100000
