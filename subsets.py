def subsets(nums):
    subsets_list = []
    def backtrack(start, current_subset):
        subsets_list.append(current_subset[:])
        for i in range(start, len(nums)):
            current_subset.append(nums[i])  
            backtrack(i + 1, current_subset)  
            current_subset.pop()
    backtrack(0, [])
    return subsets_list

