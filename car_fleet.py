class Solution:
    def carFleet(self, target,position,speed):
        arr = [(position[i], speed[i]) for i in range(len(position))]
        arr.sort(reverse=True)
        stack = []
        result = 0
        for i, j in arr:
            current_value = (target - i) / j
            if len(stack) == 0 or current_value > stack[-1]:
                stack.append(current_value)
                result = result + 1
        return result
