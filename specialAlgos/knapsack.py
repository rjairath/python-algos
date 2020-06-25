# knapsack, 0-1
# Recursive approach

# Return the max value in a knapsack
def knapsack(n, W, val, wt):
    if n == 0 or W == 0:
        return 0

    if wt[n-1] > W:
        return knapsack(n-1, W, val, wt)

    return max(val[n-1] + knapsack(n-1, W-wt[n-1], val, wt), knapsack(n-1, W, val, wt))


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapsack(n, W, val, wt))
