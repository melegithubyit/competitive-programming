import heapq

class Solution:
    def kWeakestRows(self, mat, k):
        lst = []
        output = []
        for i in mat:
            lst.append(i.count(1))
        indices = [(val, idx) for idx, val in enumerate(lst)]
        for _ in range(k):
            heapq.heapify(lst)
            val = lst.pop(0)
            for i in indices:
                value, idx = i
                if value == val:
                    output.append(idx)
                    indices.remove(i)
                    break
        return output
