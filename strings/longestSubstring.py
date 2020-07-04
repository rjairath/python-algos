# calculate all substrings of  string
# def printAllSubstrings(str):
#     n = len(str)
#     for i in range(n):
#         for j in range(i+1, n+1):
#             temp = str[i:j]
#             print(temp)


# str = 'ab'
# printAllSubstrings(str)

def maxLenSusbtring(str):
    n = len(str)
    stack = []
    stack.append(-1)

    maxLen = 0
    for i in range(n):
        if str[i] == '(':
            stack.append(i)
        elif str[i] == ')':
            stack.pop()
            if len(stack) != 0:
                top = len(stack) - 1
                maxLen = max(maxLen, i - stack[top])

            else:
                stack.append(i)
    return maxLen


str = ')))(())'
print(maxLenSusbtring(str))
