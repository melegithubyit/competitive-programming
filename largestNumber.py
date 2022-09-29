from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        def _compare(i,j):    
            if i + j > j + i:
                return -1
            elif i +j < j + i:
                return 1
            else: return 0 
        x = int("".join(sorted(map(str,nums),key = cmp_to_key(lambda i,j: _compare(i,j)))))
        return str(x)