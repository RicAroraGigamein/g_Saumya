# 1. Maximum Sum Subarray of Size K
# Problem Statement:
# You are given an array of integers and an integer K. Your task is to find the maximum possible sum of any contiguous subarray of size exactly K. A contiguous subarray consists of elements that are next to each other in the original array.
# Input:
# Array = [2, 1, 5, 1, 3, 2]
# K = 3
# Output:
# 9
def maxSumSubarray(nums, k):
    n = len(nums)
    
    # Step 1: calculate sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Step 2: slide the window
    for i in range(k, n):
        window_sum += nums[i]      # add next element
        window_sum -= nums[i-k]    # remove first element of previous window
        
        max_sum = max(max_sum, window_sum)

    return max_sum


# Driver code
arr = [2, 1, 5, 1, 3, 2]
k = 3

print(maxSumSubarray(arr, k))


#  Saumya Code
def maxSumSubarray(nums, k):
    left = 0
    window_sum = 0
    max_sum = float('-inf')

    for right in range(len(nums)):
        window_sum += nums[right]

        # When window size becomes k
        if right - left + 1 == k:
            max_sum = max(max_sum, window_sum)

            window_sum -= nums[left]
            left += 1

    return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3

print(maxSumSubarray(arr, k))



# First Negative Number in Every Window of Size K
# Problem Statement:
# You are given an array of integers that may contain both positive and negative values. For every contiguous subarray (window) of size K, find the first negative integer in that window. If a particular window does not contain any negative integer, output 0 for that window.
# Input:
# Array = [12, -1, -7, 8, -15, 30, 16, 28]
# K = 3
# Output:
# [-1, -1, -7, -15, -15, 0]

# from collections import deque
# def firstNegative(nums, k):
#     q = deque()
#     result = []
#     left = 0

#     for right in range(len(nums)):
#         # Store index if number is negative
#         if nums[right] < 0:
#             q.append(right)

#         # When window size becomes k
#         if right - left + 1 == k:
#             # First negative in window
#             if q:
#                 result.append(nums[q[0]])
#             else:
#                 result.append(0)
#             # Remove element going out of window
#             if q and q[0] == left:
#                 q.popleft()
#             left += 1
#     return result

# arr = [12, -1, -7, 8, -15, 30, 16, 28]
# k = 3
# print(firstNegative(arr, k))


# def longestSubstringKDistinct(s, k):
#     left = 0
#     max_len = 0
#     char_count = {}
#     for right in range(len(s)):
#         char_count[s[right]] = char_count.get(s[right], 0) + 1
#         # If distinct characters exceed k
#         while len(char_count) > k:
#             char_count[s[left]] -= 1

#             if char_count[s[left]] == 0:
#                 del char_count[s[left]]
#             left += 1
#         max_len = max(max_len, right - left + 1)
#     return max_len

# s = "eceba"
# k = 2

# print(longestSubstringKDistinct(s, k))



def findAnagrams(s, p):
    result = []
    p_count = {}
    window_count = {}
    for c in p:
        p_count[c] = p_count.get(c, 0) + 1

    k = len(p)

    for i in range(len(s)):
        # add current character
        window_count[s[i]] = window_count.get(s[i], 0) + 1

        # remove character leaving window
        if i >= k:
            if window_count[s[i-k]] == 1:
                del window_count[s[i-k]]
            else:
                window_count[s[i-k]] -= 1

        # compare counts
        if window_count == p_count:
            result.append(i-k+1)

    return result

s = "cbaebabacd"
p = "abc"

print(findAnagrams(s, p))