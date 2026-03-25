
# 1. Fibonacci Number
# Given an integer n, return the nth Fibonacci number using dynamic programming.
# Input
# n = 6
# Output
# 8
# Explanation
# Fibonacci sequence → 0, 1, 1, 2, 3, 5, 8



# 1. Normal Recursion (Brute Force)
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)


# 2. Memoization (Top-Down DP)
# def fib(n, dp={}):
#     if n <= 1:
#         return n
    
#     if n in dp:
#         return dp[n]
    
#     dp[n] = fib(n-1, dp) + fib(n-2, dp)
#     return dp[n]


# 3. Tabulation (Bottom-Up DP)
# def fib(n):
#     if n <= 1:
#         return n

#     dp = [0]*(n+1)
#     dp[1] = 1

#     for i in range(2, n+1):
#         dp[i] = dp[i-1] + dp[i-2]

#     return dp[n]

# 4. Space Optimized Solution
# def fib(n):
#     if n <= 1:
#         return n

#     prev2 = 0
#     prev1 = 1

#     for i in range(2, n+1):
#         curr = prev1 + prev2
#         prev2 = prev1
#         prev1 = curr

#     return prev1




# 2. Climbing Stairs
# You are climbing a staircase with n steps. Each time you can climb either 1 step or 2 steps. Find the total number of distinct ways to reach the top.
# Input
# n = 5
# Output
# 8




# 3. Coin Change (Minimum Coins)
# Given an array of coin denominations and a target amount, find the minimum number of coins needed to make the amount.
# Input
# coins = [1, 2, 5]
# amount = 11
# Output
# 3
# Explanation
# 5 + 5 + 1 = 11
# ________________________________________
# 4. Coin Change (Number of Ways)
# Given coins and a target amount, count how many different ways you can make the amount.
# Input
# coins = [1, 2, 5]
# amount = 5
# Output
# 4

def coinChangeWays(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1   # one way to make 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]
coins = [1, 2, 5]
amount = 5
print(coinChangeWays(coins, amount))


# ________________________________________
# 5. 0/1 Knapsack
# Given weights and values of items and a bag capacity, find the maximum value that can be carried.
# Input
# weights = [1, 3, 4, 5]
# values = [1, 4, 5, 7]
# capacity = 7
# Output
# 9


# def knapsack(weights, values, capacity):
#     n = len(weights)

#     dp = [[0]*(capacity+1) for _ in range(n+1)]

#     for i in range(1, n+1):
#         for w in range(1, capacity+1):

#             if weights[i-1] <= w:
#                 dp[i][w] = max(
#                     values[i-1] + dp[i-1][w - weights[i-1]],
#                     dp[i-1][w]
#                 )
#             else:
#                 dp[i][w] = dp[i-1][w]

#     return dp[n][capacity]


# weights = [1, 3, 4, 5]
# values = [1, 4, 5, 7]
# capacity = 7

# print(knapsack(weights, values, capacity))



def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0]*(capacity+1)

    for i in range(n):
        for w in range(capacity, weights[i]-1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]
print(knapsack(weights, values, capacity))
# ________________________________________
# 6. Longest Common Subsequence (LCS)
# Given two strings, find the length of their longest common subsequence.
# Input
# text1 = "abcde"
# text2 = "ace"
# Output
# 3
# Explanation
# Common subsequence → "ace"
# ________________________________________
# 7. Longest Increasing Subsequence (LIS)
# Given an array, find the length of the longest strictly increasing subsequence.
# Input
# arr = [10, 9, 2, 5, 3, 7, 101, 18]
# Output
# 4
# Explanation
# LIS → [2, 3, 7, 101]
# ________________________________________
# 8. Edit Distance
# Given two strings, find the minimum number of operations required to convert one string into another.
# Allowed operations: insert, delete, replace.
# Input
# word1 = "horse"
# word2 = "ros"
# Output
# 3
# ________________________________________
# 9. Unique Paths in Grid
# A robot is at the top-left corner of an m × n grid and can move only right or down. Find the number of unique paths to reach the bottom-right corner.
# Input
# m = 3
# n = 7
# Output
# 28
# ________________________________________
# 10. Partition Equal Subset Sum
# Given an array, determine if it can be partitioned into two subsets such that both have equal sum.
# Input
# arr = [1, 5, 11, 5]
# Output
# true
# Explanation
# Subset1 = [1, 5, 5]
# Subset2 = [11]
