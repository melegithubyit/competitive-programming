class Solution(object):
    def findJudge(self, n, trust):
        tracker = [0] * n
        for a, b in trust:
            tracker[a-1] -= 1
            tracker[b-1] += 1

        for i in range(n):
            if tracker[i] == n-1:
                return i+1
        return -1
    
# or

    # def findJudge(self, n, trust):
    #     indegree_edge = [0] * n
    #     outdegree_edge = [0] * n
    #     for a, b in trust:
    #         indegree_edge[b-1] += 1
    #         outdegree_edge[a-1] += 1

    #     for i in range(n):
    #         if indegree_edge[i] == n-1 and outdegree_edge[i] == 0:
    #             return i+1
    #     return -1
