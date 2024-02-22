class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indices = defaultdict(int)
        for idx, ele in enumerate(s):
            indices[ele] = idx + 1

        result = []
        max_val = float('-inf')

        for idx, ele in enumerate(s):
            max_val = max(max_val, indices[ele])
            if indices[ele] == idx + 1 and indices[ele] == max_val:
                result.append(idx + 1)
                max_val = 0

        for i in range(len(result) - 1, 0, -1):
            result[i] -= result[i-1]


        return result


        