
def productOfAllSubarrays(arr, start, end, ans):
    if end == len(arr):
        return ans
    if start > end:
        return productOfAllSubarrays(arr, 0, end+1, ans)
    else:
        for i in range(start, end+1):
            ans = ans * arr[i]

        print(ans)
        return productOfAllSubarrays(arr, start+1, end, ans)


def productOfAllSubarrays2(arr):
    ans = 1

    for i in range(0, len(arr)):
        product = 1
        for j in range(i, len(arr)):
            product *= arr[j]
            ans *= product

    return ans


arr = [2, 4]
n = len(arr)-1
ans = productOfAllSubarrays2(arr)
print(ans)
