import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        priorityQueue = []
        for number in nums:
            heapq.heappush(priorityQueue, number)
        pq = []
        while priorityQueue:
            value = heapq.heappop(priorityQueue)
            pq.append(value)

        wanted = pq[::-1]
        return wanted[k-1]
