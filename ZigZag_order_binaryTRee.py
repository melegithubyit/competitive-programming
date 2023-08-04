# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return None

        queue = [root]
        result = []
        counter = 1
        while queue:
            elements = []
            length = len(queue)

            for _ in range(length):
                node = queue.pop(0)
                elements.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if counter % 2 == 1:
                result.append(elements)
                counter += 1
            else:
                result.append(elements[::-1])
                counter += 1

        return result
