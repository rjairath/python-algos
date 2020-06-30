
def mergeSort(arr, x):
    l = len(arr)

    if l > 1:
        mid = (l)//2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left, x)
        mergeSort(right, x)

        i = j = k = 0

        print(left, right, 'arrays..')

        while(i < len(left) and j < len(right)):
            if left[i] % x <= right[j] % x:
                arr[k] = left[i]
                k += 1
                i += 1
            elif left[i] % x > right[j] % x:
                arr[k] = right[j]
                k += 1
                j += 1

        while(i < len(left)):
            arr[k] = left[i]
            k += 1
            i += 1

        while(j < len(right)):
            arr[k] = right[j]
            k += 1
            j += 1


def sortModuloBased(arr, k):
    mergeSort(arr, k)
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code
if __name__ == "__main__":
    value = input()
    n, k = value.split()
    n, k = int(n), int(k)

    arr = [int(j) for j in input().split()]
    sortModuloBased(arr, k)
