class Solution(object):
    import heapq
    def kClosest(self, points, k):
        def dis(a,b):
            d = (a)**2 + (b)**2
            return d
        points = [(dis(i[0],i[1]),i[0],i[1]) for i in points]
        heapq.heapify(points)
        result = []
        for i in range(k):
            x = heapq.heappop(points)
            result.append(x[1:])
        return result
