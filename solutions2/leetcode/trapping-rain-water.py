class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) == 1 or len(height) == 2:
            return 0
            
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        max_left[1] = height[0]
        max_right[-2] = height[-1]

        curr_max_left = max(height[0], height[1])
        curr_max_right = max(height[-1], height[-2])

        for i in range(2, len(height)):
            max_left[i] = curr_max_left
            curr_max_left = max(curr_max_left, height[i])
        
        for i in range(len(height) - 3, -1, -1):
            max_right[i] = curr_max_right
            curr_max_right = max(curr_max_right, height[i])
        
        for i in range(len(height)):
            max_right[i] = min(max_left[i], max_right[i])
        
        result = 0
        for idx, ele in enumerate(height):
            value = max_right[idx] - ele
            if value > 0:
                result += value

        return result

        
