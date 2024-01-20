class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        _sum, _total =  0, 0
        leftSum = [0] * len(nums)
        rightSum =  [0] * len(nums)

        for i in range(1, len(nums)):
            _sum += nums[i-1]
            leftSum[i] = _sum
        print(leftSum)
        
        nums.reverse()
        for i in range(1, len(nums)):
            _total += nums[i-1]
            rightSum[i] = _total

        rightSum.reverse()
        print(rightSum)
        counter = 0
        for i in range(len(nums)):
            if leftSum[i] != rightSum[i]:
                counter += 1
            else:
                return counter
        
        return -1





        