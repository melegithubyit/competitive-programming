class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        m =0
        n = len(plants) - 1
        waterA, waterB = capacityA, capacityB
        answer = 0
        while m < n:
            if waterA < plants[m]:
                answer += 1
                waterA = capacityA
            waterA -= plants[m]
            m += 1
            
            if waterB < plants[n]:
                answer += 1
                waterB = capacityB
            waterB -= plants[n]
            n -= 1
        
        if m == n and waterA < plants[m] and waterB < plants[m]:
            answer += 1
        return answer