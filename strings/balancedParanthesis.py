opening = {'{', '[', '('}
closing = {'}', ']', ')'}


def checkBalanced(str):
    n = len(str)
    stack = []
    for i in range(n):
        if str[i] in opening:
            stack.append(str[i])

        elif str[i] in closing:
            if len(stack) == 0:
                return False
            temp = stack.pop()

            if str[i] == '}':
                if temp != '{':
                    return False
            if str[i] == ']':
                if temp != '[':
                    return False
            if str[i] == ')':
                if temp != '(':
                    return False

    if len(stack) != 0:
        return False

    return True


expr = "{()}[]}"
if checkBalanced(expr):
    print("Balanced")
