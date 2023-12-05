class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        min_ghost_move = float('inf')
        for i in ghosts:
            ghost = i
            move = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            min_ghost_move = min(min_ghost_move, move)

        mine_move = abs(target[0]) + abs(target[1])

        if mine_move < min_ghost_move:
            return True
        return False

        

        