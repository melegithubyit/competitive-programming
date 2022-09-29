class Solution(object):
    def kthLargestNumber(self, nums, k):
        list = []
        for i in nums:
            list.append(int(i))
        for n in range(0, len(list) - 1):
            current_min_index = n
            for j in range(n + 1, len(list)):
                if list[j] < list[current_min_index]:
                    current_min_index = j
            list[n], list[current_min_index] = list[current_min_index], list[n]

        return str(list[len(list) - k])
