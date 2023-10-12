class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant, dire = [], []
        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant[0] + n)
            else:
                dire.append(dire[0] + n)
            radiant.pop(0)
            dire.pop(0)

        return "Radiant" if radiant else "Dire"
