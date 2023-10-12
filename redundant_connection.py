class Solution:
    def findRedundantConnection(self, edges):
        parent = []
        for i in range(len(edges) + 1):
            parent.append(i)

        def find(n):
            while n != parent[n]:
                n = parent[n]
            return n

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            parent[p2] = p1

        for v1, v2 in edges:
            p1, p2 = find(v1), find(v2)
            if p1 != p2:
                union(v1, v2)
            else:
                return [v1, v2]
