class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        i = 0
        j = len(people)-1
        total = 0
        count = 0
        person = 0
        while j >= i:
            if total + people[j] <= limit and person < 2:
                total += people[j]
                j -= 1
                person += 1
            elif total + people[i] <= limit and person < 2:
                total += people[i]
                i += 1
                person += 1
            else:
                count += 1
                total, person = 0, 0
        if total != 0:
            count += 1
        return count
