class Solution(object):
    def characterReplacement(self, s, k):
        dic = defaultdict(int)
        left = 0
        right = 0
        max_val = 0

        while right < len(s):
            dic[s[right]] += 1

            while (right - left + 1)-max(dic.values()) > k:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    del dic[s[left]]

                left += 1

            max_val = max(max_val, right - left + 1 )
            right += 1
        

        return max_val







