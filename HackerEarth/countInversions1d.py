# Python 3 program to count inversions in an array
# A very good O(nlogn) approach
def merge_helper():
    pass


def merge_sort(arr):
    inv_count = 0

    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        inv_count += merge_sort(L)
        inv_count += merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
                k += 1
            elif L[i] > R[j]:
                inv_count += 1
                arr[k] = R[j]
                j += 1
                k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return inv_count


# Driver Code
# Given array is
arr = [1, 20, 6, 4, 5]
n = len(arr)
result = merge_sort(arr)
print("Number of inversions are", result)
