def decimalToBinary(n):
    ans = []
    while(n > 1):
        ans.append(n % 2)
        n = n//2

    if n == 1:
        ans.append(n)

    for i in range(len(ans)-1, -1, -1):
        print(ans[i], end="")
    print('\n')

    return ans


def countingSetBits(n):
    binaryArr = decimalToBinary(n)
    counter = 0
    for i in range(0, len(binaryArr)):
        if binaryArr[i]:
            counter += 1
    return counter


def countingSetBits2(n):
    count = 0
    while(n):
        count += n & 1
        n = n >> 1
    return count


def countingSetBits3(n):
    count = 0

    while(n):
        n = n & (n-1)
        count += 1

    return count


n = 114
print(countingSetBits3(n))
