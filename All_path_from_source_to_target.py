class Solution:
    def allPathsSourceTarget(self, graph):
        all_paths = []
        n = len(graph)

        def traverse(node, path):
            if node == n - 1:
                all_paths.append(path + [node])
                return
            for neighbor in graph[node]:
                traverse(neighbor, path + [node])

        traverse(0, [])
        return all_paths
