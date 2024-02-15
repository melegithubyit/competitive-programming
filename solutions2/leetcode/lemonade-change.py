class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        store = defaultdict(int)

        for i in bills:
            if i == 5:
                store[i] += 1
            elif i == 10:
                if 5 not in store:
                    return False
                store[i] += 1
                store[5] -= 1
                if store[5] == 0:
                    del store[5]
            else:
                if 5 not in store:
                    return False
                if 10 in store:
                    store[10] -= 1
                    if store[10] == 0:
                        del store[10]
                    store[5] -= 1
                    if store[5] == 0:
                        del store[5]
                else:
                    if store[5] < 3:
                        return False
                    store[5] -= 3
                    if store[5] == 0:
                        del store[5]
                store[i] += 1

        return True
                 