class Solution:
    def isBipartite(self, graph):
        colors = [0] * len(graph)

        for node in range(len(graph)):
            if colors[node] == 0:
                colors[node] = 1
                queue = [node]

                while queue:
                    curr = queue.pop(0)
                    for neighbor in graph[curr]:
                        if colors[neighbor] == 0:
                            colors[neighbor] = 3 - colors[curr]
                            queue.append(neighbor)
                        elif colors[neighbor] == colors[curr]:
                            return False 

        return True 
