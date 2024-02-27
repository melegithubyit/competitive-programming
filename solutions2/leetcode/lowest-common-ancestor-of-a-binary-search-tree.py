# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p    
        self.q = q

        def helper(root):
            if not root:
                return None
            
            if root.val == self.p.val or root.val == self.q.val:
                return root
            
            if (root.val > self.p.val and root.val < self.q.val) or (root.val < self.p.val and root.val > self.q.val):
                return root

            if self.p.val > root.val and self.q.val > root.val:
                return helper(root.right)

            if self.p.val < root.val and self.q.val < root.val:
                return helper(root.left)

        return helper(root)

