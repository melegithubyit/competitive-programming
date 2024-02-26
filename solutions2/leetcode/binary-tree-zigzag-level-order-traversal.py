# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque()
        queue.append(root)
        direction = "left"

        while queue:
            n = len(queue)
            temp = []
            if direction == "left":
                for i in range(n):
                    node = queue.popleft()
                    if node:
                        temp.append(node.val)
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
                direction = "right"
            
            elif direction == "right":
                for i in range(n):
                    node = queue.pop()
                    if node:
                        temp.append(node.val)
                        if node.right:
                            queue.appendleft(node.right)
                        if node.left:
                            queue.appendleft(node.left)

                direction = "left"
            
            result.append(temp)


        return result            



        