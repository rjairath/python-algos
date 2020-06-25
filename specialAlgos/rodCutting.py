def maxPrice(startingIndex, n, priceArr):
    if (startingIndex + 1) > n:
        return 0

    return max(maxPrice(startingIndex+1, n, priceArr),
               priceArr[startingIndex] + maxPrice(startingIndex+1, n-(startingIndex+1), priceArr))


def maxPriceDP(price, n):
    val = [0 for x in range(0, n+1)]

    for i in range(1, n+1):
        max_val = -1000
        for j in range(i):
            max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val

    return val[n]


arr = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(arr)

x = maxPriceDP(arr, size)
print(x)
