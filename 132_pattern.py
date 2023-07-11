class Solution(object):
    def find132pattern(self, nums):
        stack = []
        s3 = float('-inf')

        for num in reversed(nums):
            if num < s3:
                return True
            while stack and stack[-1] < num:
                s3 = stack.pop()
            stack.append(num)

        return False


# [2, 4, 1, 3]

# num = 1

# stack = [4]
# s3 =2
