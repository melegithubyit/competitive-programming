class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        tracker = defaultdict(int)
        left = 0

        min_length = float('inf')
        flag = False

        for right in range(len(cards)):
            tracker[cards[right]] += 1

            while left <= right and right - left + 1 > len(tracker):
                min_length = min(min_length, right - left + 1)
                flag = True
                tracker[cards[left]] -= 1
                if tracker[cards[left]] == 0:
                    del tracker[cards[left]]
                
                left += 1

        if flag:return min_length
        return -1

            

        

        