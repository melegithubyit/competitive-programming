class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        store = defaultdict(int)
        result = 0
        for i in answers:
            store[i] += 1
        print(store)

        for i in store:
            if i == 0:
                result += store[i]
            else:
                if store[i] <= i + 1:
                    result += (i+1)
                else:
                    val = store[i] // (i + 1)
                    rem = store[i] % (i + 1)
                    result += (val * (i+1))
                    if rem != 0:
                        result += (i+1)

        return result 
