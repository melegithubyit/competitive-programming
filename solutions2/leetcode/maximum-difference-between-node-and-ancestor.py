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
        self.ans = 0

        def helper(root, max_val, min_val):

            if not root:
                self.ans = max(self.ans, max_val - min_val)
                return 
            
            max_val = max(max_val, root.val)
            min_val = min(min_val, root.val)
        
            if root and not root.left and not root.right:
                self.ans = max(self.ans, max_val - min_val)
                return 
            

            left = helper(root.left, max_val, min_val)
            right = helper(root.right, max_val, min_val)
        

        helper(root, self.max_val, self.min_val)
        return self.ans
        # return max(left, right)
        
