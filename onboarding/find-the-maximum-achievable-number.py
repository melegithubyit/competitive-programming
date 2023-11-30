class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        val = num + t
        return (val * 2) - num
        