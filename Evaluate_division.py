from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i in range(len(equations)):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1 / values[i]
            
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if end in graph[start]:
                return graph[start][end]
            for neighbor in graph[start]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    res = dfs(neighbor, end, visited)
                    if res != -1.0:
                        return graph[start][neighbor] * res
            return -1.0

        output = []
        for query in queries:
            output.append(dfs(query[0], query[1], set([query[0]])))

        return output
