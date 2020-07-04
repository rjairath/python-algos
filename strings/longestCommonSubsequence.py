
# lcs in str1 till i, in str2 till j
def lcs(str1, str2, i, j):
    n1 = len(str1)
    n2 = len(str2)

    if i >= n1 or j >= n2:
        return 0

    if str1[i] == str2[j]:
        return 1 + lcs(str1, str2, i+1, j+1)

    else:
        return max(lcs(str1, str2, i+1, j), lcs(str1, str2, i, j+1))

# return the length of longest common subsequence in 2 strings


def lcsDP(str1, str2, i, j):
    n1 = len(str1)
    n2 = len(str2)
    dp = [[0 for i in range(n2+1)] for j in range(n1+1)]

    for i in range(n1+1):
        dp[i][0] = 0

    for j in range(n2+1):
        dp[0][j] = 0

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # return dp[n1][n2]
    # find the lcs now
    return printLCS(dp, n1, n2, str1, str2)


def printLCS(dp, row, col, str1, str2):
    stack = []
    i = row
    j = col

    while(i > 0 and j > 0):
        if dp[i][j] == dp[i-1][j-1] + 1 and str1[i-1] == str2[j-1]:
            stack.append(str1[i-1])
            i -= 1
            j -= 1

        elif dp[i][j] == dp[i][j-1]:
            j -= 1

        elif dp[i][j] == dp[i-1][j]:
            i -= 1

    temp = ''
    while(len(stack) > 0):
        x = stack.pop()
        temp += x

    return temp


str1 = 'abcdaf'
str2 = 'acbcf'

l = lcsDP(str1, str2, 0, 0)
print(l)
