class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counts = [0] * 121
        for age in ages:
            counts[age] += 1

        total_requests = 0
        for ageA in range(1, 121):
            countA = counts[ageA]
            for ageB in range(1, 121):
                countB = counts[ageB]

                if (
                    ageB <= 0.5 * ageA + 7 or
                    ageB > ageA or
                    (ageB > 100 and ageA < 100)
                ):
                    continue
                total_requests += countA * countB
                if ageA == ageB:
                    total_requests -= countA

        return total_requests
