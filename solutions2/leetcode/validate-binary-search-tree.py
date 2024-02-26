# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lst = []

        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            lst.append(root.val)
            inorder(root.right)

        inorder(root)
        return lst == sorted(lst) and len(lst) == len(set(lst))