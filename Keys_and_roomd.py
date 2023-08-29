class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True

        def dfs(room):
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    dfs(key)

        dfs(0)

        return all(visited)
