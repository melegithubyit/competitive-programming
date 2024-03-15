class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_valid(num, weights, days):
            counter = 1
            run_sum = 0

            for i in range(len(weights)):
                run_sum += weights[i]
                if run_sum > num:
                    counter += 1
                    run_sum = weights[i]
                    if run_sum > num:
                        return False
                
            return counter <= days
                

        left = max(weights)
        right = 2**32
        while left < right:
            avg = (left + right) // 2
            if is_valid(avg, weights, days):
                right = avg
            else:
                left = avg + 1
            
        return left



                
                
