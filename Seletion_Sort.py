def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Assume the current index is the minimum
        min_index = i

        # Find the minimum element in remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)

print("Sorted array:", sorted_arr)
