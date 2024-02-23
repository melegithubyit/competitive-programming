class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        R_count = 0
        D_count = 0

        R_queue = deque()
        D_queue = deque()

        for idx, ele in enumerate(senate):
            if ele == 'R':
                R_queue.append((ele, idx))
            else:
                D_queue.append((ele, idx))

        while R_queue and D_queue:
            _, idxR = R_queue.popleft()
            _, idxD = D_queue.popleft()

            if idxR < idxD:
                R_queue.append(('R', n + idxR))
            else:
                D_queue.append(('D', n + idxD))


        if R_queue:
            return "Radiant"
        else:
            return "Dire"

        