# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], res="") -> int:

        if not root.left and not root.right:
            res += str(root.val)
            return int(res)

        res += str(root.val)
        left_sum = 0
        right_sum = 0

        if root.left:
            left_sum = self.sumNumbers(root.left, res)

        if root.right:
            right_sum = self.sumNumbers(root.right, res)

        return left_sum + right_sum

        