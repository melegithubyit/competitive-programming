class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curr_min_operation = blocks[:k].count('W')
        min_ope = curr_min_operation

        left = 0

        for right in range(k, len(blocks)):
            if blocks[right] == 'W':
                curr_min_operation += 1
            if blocks[left] == 'W':
                curr_min_operation -= 1

            min_ope = min(min_ope, curr_min_operation)
            left += 1

        return min_ope

        