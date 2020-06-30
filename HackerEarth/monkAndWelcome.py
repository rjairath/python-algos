

def printNewArray(A, B, n):
    for i in range(n):
        print(A[i]+B[i], end=" ")


n = int(input())
A = []
B = []

A = list(map(int, input().split()))


B = list(map(int, input().split()))

printNewArray(A, B, n)
