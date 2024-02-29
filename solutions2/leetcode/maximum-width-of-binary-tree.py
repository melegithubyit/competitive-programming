# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([(root, 0)])
        maxwidth = 0

        while queue:
            result = []

            for i in range(len(queue)):

                node, number = queue.popleft()
                result.append(number)
                
                if node.left:
                    queue.append((node.left, number*2+1))

                if node.right:
                    queue.append((node.right, number*2+2))

            maxwidth = max(maxwidth, result[-1] - result[0] + 1)


        return maxwidth