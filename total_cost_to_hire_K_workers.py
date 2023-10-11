import heapq
class Solution:
    def totalCost(self, costs, k: int, candidates: int) -> int:
        cost = 0
        hired = 0
        n = len(costs)
        i = 0
        j = n - 1
        LHeap = []
        RHeap = []
        while hired < k:
            while len(LHeap) < candidates and i <= j:
                heapq.heappush(LHeap, costs[i])
                i += 1
            while len(RHeap) < candidates and j >= i:
                heapq.heappush(RHeap, costs[j])
                j -= 1
            if len(LHeap):
                l = LHeap[0]
            else:
                l = float("inf")
            if len(RHeap):
                r = RHeap[0]
            else:
                r = float("inf")

            if l <= r:
                cost += heapq.heappop(LHeap)
            else:
                cost += heapq.heappop(RHeap)
            hired += 1
        return cost
