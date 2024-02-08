class Solution(object):
    def carPooling(self, trips, capacity):
        lst = []
        for ppl, pick, drop in trips:
            lst.append([pick, ppl, 1])
            lst.append([drop, ppl, 0])

        lst.sort(key = lambda x: (x[0], x[2]))
        curr = 0

        for time, ppl, pickup in lst:
            if pickup:
                curr += ppl

            else:
                curr -= ppl
            if curr > capacity: return False

        return True



        