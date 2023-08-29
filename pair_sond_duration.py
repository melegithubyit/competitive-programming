class Solution:
    def numPairsDivisibleBy60(self, time):
        count = 0
        remainders = [0] * 60

        for t in time:
            remainder = t % 60
            complement = (60 - remainder) % 60

            count += remainders[complement]
            remainders[remainder] += 1

        return count
