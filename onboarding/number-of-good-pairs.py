class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashTable = defaultdict(int)
        counter = 0
        for i in nums:
            if i not in hashTable:
                hashTable[i] += 1
            
            else:
                counter += hashTable[i]
                hashTable[i] += 1

            
        return counter


        