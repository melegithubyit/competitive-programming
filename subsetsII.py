class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        subsets = []

        def generateSubsets(nums, subset, startIndex):
            subsets.append(subset[:])

            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                generateSubsets(nums, subset, i + 1)
                subset.pop()

        generateSubsets(nums, [], 0)
        return subsets
