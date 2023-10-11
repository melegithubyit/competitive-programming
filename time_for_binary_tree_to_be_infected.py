# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
class Solution:
    def amountOfTime(self, root, start) -> int:
        dic = defaultdict(set)
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    dic[node.left.val].add(node.val)
                    dic[node.val].add(node.left.val)
                    queue.append(node.left)
                if node.right:
                    dic[node.right.val].add(node.val)
                    dic[node.val].add(node.right.val)
                    queue.append(node.right)

        q = deque([start])
        visited = set([start])
        res = -1
        while q:
            res += 1
            for j in range(len(q)):
                node = q.popleft()
                for next_node in dic[node]:
                    if next_node in visited:
                        continue
                    visited.add(next_node)
                    q.append(next_node)
        return res
