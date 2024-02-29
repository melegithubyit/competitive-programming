class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        store = defaultdict(list)
        self.col = 0
        self.row = 0

        def helper(root, row, col):
            if not root:
                return 
            
            store[col].append((row, root.val))  
            helper(root.left, row + 1, col - 1)
            helper(root.right, row + 1, col + 1)

        helper(root, self.row, self.col)
        result = []
        sorted_store = sorted(store.items(), key=lambda x: x[0]) 
        
        for _, lst in sorted_store:
            lst.sort(key=lambda x: (x[0], x[1]))  
            result.append([val for _, val in lst]) 

        return result