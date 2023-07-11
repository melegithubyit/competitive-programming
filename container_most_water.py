class Solution:
    def maxArea(height) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:
                current = height[left]
            else:
                current = height[right]
            distance = right - left
            area = current * distance
            if area > max_area:
                max_area = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
