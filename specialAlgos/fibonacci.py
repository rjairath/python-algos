def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


def fib2(n):
    a = 0
    b = 1

    if n <= 1:
        return n

    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b


def fib3(n, fibArray):
    # Using DP

    # fibArray = [0, 1]

    # while len(fibArray) < n+1
    # fibArray.append(0)

    if n <= 1:
        return n
    else:
        if fibArray[n-1] == 0:
            fibArray[n-1] = fib3(n-1, fibArray)

        # if fibArray[n-2] == 0:
        #     fibArray[n-2] = fib3(n-2)

        fibArray[n] = fibArray[n-1] + fibArray[n-2]

        return fibArray[n]


def fib_helper(n):
    fibArray = [0, 1]
    while len(fibArray) < n+1:
        fibArray.append(0)

    return fib3(n, fibArray)


print(fib_helper(500))
