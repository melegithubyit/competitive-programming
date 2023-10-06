def counting_sort(arr):
    m = min(arr)
    n = max(arr)
    count = [0] * (n - m + 1)

    for num in arr:
        count[num - m] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]
        
    sorted_arr = [0] * len(arr)
    for num in reversed(arr):
        sorted_arr[count[num - m] - 1] = num
        count[num - m] -= 1

    return sorted_arr

