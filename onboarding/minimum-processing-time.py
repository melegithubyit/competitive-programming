class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        max_val = float('-inf')

        processorTime.sort()
        tasks.sort(reverse = True)

        for i in range(len(processorTime)):
            for j in range(4*i, (4*i) + 4):
                _sum = processorTime[i] + tasks[j]
                max_val = max(max_val, _sum)

        return max_val
