# longest palindromic subsequence
# i and j are start and end index
def lps(seq, i, j):
    if i == j:
        return 1

    if seq[i] == seq[j] and i + 1 == j:
        return 2

    if seq[i] == seq[j]:
        return 2 + lps(seq, i+1, j-1)

    else:
        return max(lps(seq, i+1, j), lps(seq, i, j-1))


def lpsDP(s):
    n = len(s)
    dp = [[0 for i in range(n)] for j in range(n)]
    # length = 1
    for i in range(n):
        dp[i][i] = 1

    # length = 2
    for i in range(0, n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 2
        else:
            dp[i][i+1] = 1

    # length >= 3
    l = 3
    while(l <= n):
        for i in range(0, n-l+1):
            j = i + l - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        l += 1

    return dp[0][n-1]


seq = 'GEEKSFORGEEKS'
n = len(seq)
# l = lps(seq, 0, n-1)
l = lpsDP(seq)
print(l)
