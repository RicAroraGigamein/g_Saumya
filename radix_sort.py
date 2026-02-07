def counting_sort(arr, exp):
    n = len(arr)

    output = [0] * n        # Output array
    count = [0] * 10       # Digits 0–9

    # Count occurrences of digits
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Convert count → cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array (right to left for stability)
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy back
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_val = max(arr)

    exp = 1   # 1 → units, 10 → tens, 100 → hundreds

    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr


# Example
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Sorted array:", radix_sort(arr))
