class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        max_val = max(candies)
        for i in candies:
            if i + extraCandies >= max_val:
                res.append(True)
            else:
                res.append(False)

        return res
        