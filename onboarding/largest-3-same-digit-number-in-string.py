class Solution:
    def largestGoodInteger(self, num: str) -> str:
        dic = defaultdict(int)
        flag = False
        for i in range(3):
            dic[num[i]] += 1

        left = 0
        right = 3
        max_val = 0

        if len(dic) == 1:
            val = num[:3]
            if val == '000':
                flag = True
            max_val = max(max_val, int(val))
            if max_val != 0:
                flag = False
        


        while right < len(num):
            dic[num[right]] += 1
            dic[num[left]] -= 1
            if dic[num[left]] == 0:
                del dic[num[left]]
            
            left += 1
            right += 1

            if len(dic) == 1:
                val = num[left : right]
                if val == '000':
                    flag = True
                max_val = max(max_val, int(val))
                if max_val != 0:
                    flag = False
        if flag:
            return '000'

        if max_val != 0:
            return str(max_val)
        return ""

        