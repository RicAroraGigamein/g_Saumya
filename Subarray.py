# arr = [1, 2, 3]

# n = len(arr)

# for start in range(n):
#     for end in range(start, n):
#         # Print subarray from start to end
#         for k in range(start, end + 1):
#             print(arr[k], end=" ")
#         print()



# arr = [1, 2, 3]
# subarrays = []

# n = len(arr)

# for start in range(n):
#     for end in range(start, n):
#         subarrays.append(arr[start:end+1])

# print(subarrays)


# arr = [1, 2, 3]

# n = len(arr)

# for start in range(n):
#     for end in range(start, n):
#         print(arr[start:end+1])



# [5, -3, 5]

# for l in range(n):

#     (i+1)%n



#     def maxSubarraySumCircular(nums):
#     n = len(nums)
    

# 918. Maximum Sum Circular Subarray
    # Step 1: Duplicate array
    # dup = nums * 2
    
    # max_sum = float('-inf')
    
    # # Step 2: Generate all subarrays
    # for i in range(2 * n):
    #     curr_sum = 0
        
    #     # Length should not exceed n
    #     for j in range(i, i + n):
    #         curr_sum += dup[j]
    #         max_sum = max(max_sum, curr_sum)
    
    # return max_sum



# 918. Maximum Sum Circular Subarray (without space complexity)

def maxsumcircular(nums):
    n=len(nums)
    ans=float('-inf')

    for i in range(n):
        s=0
        for 1 in range(n):
            s+=nums[(i+1)%n]
            ans=max(ans,s)

    return ans


nums=[5,-3,5]
result=maxsumcircular(nums)
print(result)

