# def bucket_sort(arr):
#     n = len(arr)

#     # Create empty buckets
#     buckets = [[] for _ in range(n)]

#     # Put array elements into different buckets
#     for num in arr:
#         index = int(num * n)   # Bucket index
#         buckets[index].append(num)

#     # Sort individual buckets
#     for bucket in buckets:
#         bucket.sort()

#     # Concatenate all buckets
#     sorted_arr = []
#     for bucket in buckets:
#         sorted_arr.extend(bucket)

#     return sorted_arr


# # Example 
# arr = [0.78, 0.17, 0.39, 0.26]
# # arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
# print("Sorted array:", bucket_sort(arr))




def bucket_sort(arr):
    n = len(arr)

    if n == 0:
        return arr

    # Step 1: Find min and max
    min_val = min(arr)
    max_val = max(arr)

    # Step 2: Create buckets
    buckets = [[] for _ in range(n)]

    # Step 3: Put elements into buckets
    for num in arr:
        index = int((num - min_val) / (max_val - min_val + 1) * n)
        buckets[index].append(num)

    # Step 4: Sort each bucket
    for bucket in buckets:
        bucket.sort()

    # Step 5: Merge buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr


# # Example
# arr = [1, 3, 4, 2, 6]
# print("Sorted array:", bucket_sort(arr))


# def bucket_sort_simple(arr):
#     max_val = max(arr)

#     # Create buckets
#     buckets = [[] for _ in range(max_val + 1)]

#     # Insert elements
#     for num in arr:
#         buckets[num].append(num)

#     # Merge
#     sorted_arr = []
#     for bucket in buckets:
#         sorted_arr.extend(bucket)

#     return sorted_arr


# arr = [1, 3, 4, 2, 6]
# print(bucket_sort_simple(arr))
