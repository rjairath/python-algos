dict = ['a', 'e', 'i', 'o', 'u']


def findLongestSubstr(s):
    maxLength = 0
    i = 0
    while(i < len(s)):
        j = i
        count = 0
        while(j < len(s) and s[j] in dict):
            count += 1
            j += 1
            if count > maxLength:
                maxLength = count

        i = j+1
    return maxLength


if __name__ == '__main__':
    s = input()
    l = findLongestSubstr(s)

    print(l)
