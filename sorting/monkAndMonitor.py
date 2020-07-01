from collections import defaultdict


def calcMaxDiff(arr):
    counter = defaultdict(int)
    distinct_heights = []

    for i in range(len(arr)):
        if counter[arr[i]] == 0:
            distinct_heights.append(arr[i])
        counter[arr[i]] += 1

    distinct_heights.sort()

    # max_height = -1
    # for i in range(len(distinct_heights)-1):
    #     for j in range(i+1, len(distinct_heights)):
    #         h1 = distinct_heights[i]
    #         h2 = distinct_heights[j]
    #         if abs(counter[h1] - counter[h2]) > max_height:
    #             max_height = abs(counter[h1] - counter[h2])
    n = len(distinct_heights)
    ans = 0
    minFreq = n+1
    for i in range(n):
        currFreq = counter[distinct_heights[i]]
        ans = max(ans, currFreq - minFreq)
        minFreq = min(minFreq, currFreq)

    return ans


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        # n = int(input())
        # arr = [int(j) for j in input().split()]
        arr = [3, 1, 3, 2, 3, 2]
        h = calcMaxDiff(arr)
        print(h)
