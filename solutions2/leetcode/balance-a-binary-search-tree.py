# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr=[]
        def traverse(root):
            if not root:
                return None
            
            traverse(root.left)
            if root:
                arr.append(root.val)
            traverse(root.right)
        
        traverse(root)
        arr.sort()


        def helper(arr):
            if not arr:
                return
            
            mid = len(arr) // 2
            node = TreeNode(arr[mid])
            node.left = helper(arr[:mid])
            node.right = helper(arr[mid+1:])

            return node
        
        return helper(arr)
