class Solution:
    def findCenter(self, edges) -> int:
        [target1, target2] = edges[0]
        if target1 in edges[1]:
            return target1
        return target2
