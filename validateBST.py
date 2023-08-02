# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        inorder_traversal = inorder(root)
        return inorder_traversal == sorted(inorder_traversal) and len(set(inorder_traversal)) == len(inorder_traversal)
