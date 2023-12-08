class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winners = defaultdict(int)
        loosers = defaultdict(int)

        for i in matches:
            win, loss = i
            winners[win] += 1
            loosers[loss] += 1

        print(winners)
        print(loosers)

        winner = []
        looser = []

        for i in winners:
            if i not in loosers:
                bisect.insort_left(winner, i)
        
        for i in loosers:
            if loosers[i] == 1:
                bisect.insort_left(looser, i)


        return [winner, looser]

        



        