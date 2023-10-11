import heapq
class Solution:
    def maxEvents(self, events) -> int:
        events.sort()
        lst = []
        j = 0
        answer = 0
        for i in range(1, 10**5 + 1):
            while j < len(events) and events[j][0] <= i:
                heapq.heappush(lst, events[j][1])
                j += 1
            while lst and lst[0] < i:
                heapq.heappop(lst)
            if lst:
                heapq.heappop(lst)
                answer += 1
        return answer