class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        length = len(nums)
        visited = set()

        for index in range(length):
            if index in visited: 
                continue

            count = {index}
            num = nums[index]
            if num >= 0:
                sign = 1
            else:
                sign = -1

            new_index = (index+num) % length
            
            while new_index != index and nums[new_index]*sign >= 0:
                if new_index in count:
                    return True

                count.add(new_index)
                visited.add(new_index)
                index = new_index
                num = nums[index]

                new_index = (new_index+num) % length

        return False