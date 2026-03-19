
# count subarray sum=k
def subarraySum(nums, k):
    prefix = 0
    count = 0
    hashmap = {0:1}
    for num in nums:
        prefix += num
        if prefix - k in hashmap:
            count += hashmap[prefix - k]
        hashmap[prefix] = hashmap.get(prefix,0) + 1
    return count



# without hashmap
def subarraySum(nums, k):
    n = len(nums)
    prefix = [0]*n
    prefix[0] = nums[0]
    for i in range(1,n):
        prefix[i] = prefix[i-1] + nums[i]
    count = 0
    for i in range(n):
        for j in range(i,n):
            if i == 0:
                curr_sum = prefix[j]
            else:
                curr_sum = prefix[j] - prefix[i-1]
            if curr_sum == k:
                count += 1
    return count
nums = [1,1,1]
k = 2

print(subarraySum(nums,k))