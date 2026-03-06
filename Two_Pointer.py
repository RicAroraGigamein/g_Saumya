# Q1. Remove duplicates from a sorted array
# Problem Statement:
# Given a sorted integer array, remove the duplicates in-place such that each element appears only once and return the new length.
# Input:
# arr = [1, 1, 2]
# Output:
# 2

# def removeDuplicates(arr):
#     if len(arr) == 0:
#         return 0
#     i = 0
#     for j in range(1, len(arr)):
#         if arr[j] != arr[i]:
#             i += 1
#             arr[i] = arr[j]

#     return i + 1

# arr = [1, 1, 2]
# length = removeDuplicates(arr)
# print(length)
# print(arr[:length])



# Q2. Move all zeros to the end
# Problem Statement:
# Given an integer array, move all zeros to the end while maintaining the relative order of non-zero elements.
# Input:
# arr = [0, 1, 0, 3, 12]
# Output:
# [1, 3, 12, 0, 0]

def moveZeroes(arr):
    i = 0

    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    return arr


arr = [0, 1, 0, 3, 12]
print(moveZeroes(arr))