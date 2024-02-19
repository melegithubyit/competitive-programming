class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = [0] * len(nums2)
        store = defaultdict(int)
        stack = []
        stack.append(nums2[-1])
        temp[-1] = -1
        ans = []

        for idx, ele in enumerate(nums2):
            store[ele] = idx

        for i in range(len(nums2) - 2, -1, -1):
            
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            
            if stack:
                temp[i] = stack[-1]
            else:
                temp[i] = -1
            
            stack.append(nums2[i])

        for i in nums1:
            ans.append(temp[store[i]])

        return ans