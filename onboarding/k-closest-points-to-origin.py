class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def calDist(lst: list[list]) -> int:
            x, y = lst
            return (x**2 + y**2) ** 0.5

        points.sort(key = lambda x: calDist(x))

        ans = []
        counter = 0 

        for i in points:
            if counter == k:
                break
            ans.append(i)
            counter += 1

        return ans


        