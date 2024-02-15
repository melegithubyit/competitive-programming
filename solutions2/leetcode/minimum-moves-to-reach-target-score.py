class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0 or target == 1:
            return target - 1
        
        store = [target]
        for i in range(maxDoubles):
            store.append(store[-1] // 2)
            if store[-1] == 1:break

        store = store[::-1]
        min_moves = 0

        for idx, ele in enumerate(store):
            if idx == 0:
                min_moves += ele
                min_moves += (store[idx + 1] - (2 * ele))
                
            else:
                if idx == len(store) - 1:
                    break
                min_moves += 1
                min_moves += (store[idx + 1] - (2 * ele))

        return min_moves

        
