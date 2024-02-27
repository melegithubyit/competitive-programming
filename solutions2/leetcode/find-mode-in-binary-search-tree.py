# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        hashT = defaultdict(int)

        def helper(root):
            if not root:
                return
            
            helper(root.left)
            hashT[root.val] += 1
            helper(root.right)

        helper(root)
        lst = []
        result = []
        sorted_hash = sorted(hashT.items(), key = lambda x: (x[1], x[0]), reverse=True)
        for key, val in sorted_hash:
            if not lst:
                result.append(key)
                lst.append(val)
            else:
                if val == lst.pop():
                    result.append(key)
                    lst.append(val)
                else:
                    break
        
        return result

            
        
