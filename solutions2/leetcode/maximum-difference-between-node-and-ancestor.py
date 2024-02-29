# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.max_val = float('-inf')
        self.min_val = float('inf')

        def helper(root, max_val, min_val):

            if not root:
                return max_val - min_val

            max_val = max(max_val, root.val)
            min_val = min(min_val, root.val)   


            left = helper(root.left, max_val, min_val)
            right = helper(root.right, max_val, min_val)

            return max(left, right)

        return helper(root, self.max_val, self.min_val)

        
