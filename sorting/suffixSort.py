
def kthSmallestSuffix(str, k):
    suffixArr = []
    for i in range(len(str)):
        suffixArr.append(str[i:])

    suffixArr = sorted(suffixArr)
    return suffixArr[k-1]


if __name__ == "__main__":
    value = input()
    str, k = value.split(" ")
    k = int(k)

    print(kthSmallestSuffix(str, k))
