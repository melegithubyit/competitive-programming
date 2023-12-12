class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        invalid = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                invalid.add(fronts[i])

        
        min_val = float('inf')
        flag = False

        for i in range(len(fronts)):
            if fronts[i] not in invalid:
                min_val = min(min_val, fronts[i])
                flag = True

            if backs[i] not in invalid:
                min_val = min(min_val, backs[i])
                flag = True

        
        if flag:
            return min_val

        return 0

            

