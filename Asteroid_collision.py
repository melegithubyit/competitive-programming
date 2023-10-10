class Solution:
    def asteroidCollision(self, asteroids):
        stk = []
        for i in asteroids:
            while stk and i < 0 and stk[-1] > 0:
                if abs(i) > stk[-1]:
                    stk.pop()
                    continue
                elif abs(i) == stk[-1]:
                    stk.pop()
                break
            else:
                stk.append(i)
        return stk
