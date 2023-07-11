def maxOperations(nums, k):
    counting = dict()
    operations = 0
    for i in nums:
        counting[i] = counting.get(i, 0) + 1

    for num in nums:
        complement = k - num
        counting[num] = counting.get(num, 0)
        counting[complement] = counting.get(complement, 0)
        if counting[num] > 0 and counting[complement] > 0:
            if num == complement and counting[num] < 2:
                continue

            counting[num] -= 1
            counting[complement] -= 1
            operations += 1

    return operations


print(maxOperations([3, 1, 3, 4, 3], 6))
