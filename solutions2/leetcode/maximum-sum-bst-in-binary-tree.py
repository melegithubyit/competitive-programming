# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        maxsum = 0
        
        def validate(root):
            nonlocal maxsum
            if root == None:
                return float('inf'), float('-inf'), 0, True

            minl, maxl, suml, statusl = validate(root.left)
            minr, maxr, sumr, statusr = validate(root.right)

            if (statusl and statusr) and (maxl < root.val < minr):
                maxsum = max(maxsum, suml + root.val + sumr)
                return min(minl, root.val), max(maxr, root.val), suml + root.val + sumr, 1

            return None, None, None, False
        
        validate(root)

        return maxsum
