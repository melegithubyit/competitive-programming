import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            diff = x - y
            if diff != 0:
                heapq.heappush(max_heap, -diff)

        return -max_heap[0] if max_heap else 0
