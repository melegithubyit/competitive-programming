class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        total = 0
        prev_value = None
        for symbol in s:
            value = symbol_values[symbol]
            if prev_value is not None and prev_value < value:
                total -= 2 * prev_value  
            total += value
            prev_value = value
        return total


