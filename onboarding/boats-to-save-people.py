class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        counter = 0
        ps = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            counter += 1

        return counter

