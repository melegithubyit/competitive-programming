class Solution:
    def average(self, salary: List[int]) -> float:
        max_val = max(salary)
        min_val = min(salary)
        total = sum(salary) - max_val - min_val
        n = len(salary) - 2
        return (total / (n)) + 0.00000
        