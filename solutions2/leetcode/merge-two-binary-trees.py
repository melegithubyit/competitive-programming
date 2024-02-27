# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(root1, root2):
            if not root1 and not root2:
                return 
            if root1 and not root2:
                return root1
            if root2 and not root1:
                return root2

            if root1 and root2:
                Node = TreeNode(root1.val + root2.val)
                Node.left = helper(root1.left, root2.left)
                Node.right = helper(root1.right, root2.right)
                
                return Node

        return helper(root1, root2)
            


