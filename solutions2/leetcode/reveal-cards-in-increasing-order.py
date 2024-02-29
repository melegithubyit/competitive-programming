class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if len(deck) == 1:
            return deck
        
        deck.sort(reverse = True)
        starting = [deck[1], deck[0]]
        result = deque(starting)

        def swap(lst):
            left = len(lst) - 2
            right = len(lst) - 1
            while left >= 0:
                lst[left], lst[right] = lst[right], lst[left]
                left -= 1
                right -= 1
            

        for i in range(2, len(deck)):
            swap(result)
            result.appendleft(deck[i])
        
        return result




