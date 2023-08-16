from collections import defaultdict


class Solution(object):
    def validPath(self, n, edges, source, destination):
        if source == destination:
            return True

        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        queue = [source]
        visited = set()
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour == destination:
                    return True
                else:
                    if neighbour not in visited and neighbour not in queue:
                        queue.append(neighbour)

        return False
