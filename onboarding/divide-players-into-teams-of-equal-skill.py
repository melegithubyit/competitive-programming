class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        left = 0
        right = len(skill) - 1
        ans = 0

        total = skill[-1] + skill[0]
        flag = False

        while left < right:
            _sum = skill[left] + skill[right]
            prod = skill[left] * skill[right]

            if _sum == total:
                right -= 1
                left += 1
                total = _sum
                ans += prod
            else:
                flag = True
                break
        if flag:
            return -1
        return ans
