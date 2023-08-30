class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        provinces = 0
        visited = [False] * n

        def dfs(currCity):
            visited[currCity] = True
            for i in range(n):
                if isConnected[currCity][i] == 1 and not visited[i]:
                    dfs(i)

        for city in range(n):
            if not visited[city]:
                provinces += 1
                dfs(city)

        return provinces
