class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # lst = [0] * (len(nums) + 1)
        zero_ = nums.count(0)
        one_ = nums.count(1)
        dic = {}
        dic[0] = one_
        dic[len(nums)] = zero_

        zero_count = 0
        one_count = nums.count(1)

        for i in range(1, len(nums)):
            if nums[i-1] == 0:
                zero_count += 1
            else:
                one_count -= 1

            _sum = one_count + zero_count
            dic[i] = _sum

        sorted_dic = dict(sorted(dic.items(), key = lambda x: x[1], reverse = True))
        # print(sorted_dic)
        # lst = [1,2,3,2,3]
        # dic = { 0: 1, 1:2, 2:3, 3:2, 4:3}

        res = []

        for i in sorted_dic:
            if not res:
                res.append(i)
            else:
                if sorted_dic[i] == sorted_dic[res[-1]]:
                    res.append(i)
                else:
                    break
        return res


        

        