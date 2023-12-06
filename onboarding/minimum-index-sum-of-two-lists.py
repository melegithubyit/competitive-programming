class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        common = []
        for i in list1:
            if i in list2:
                common.append(i)

        for i in common:
            dic[i] = (list1.index(i) + list2.index(i))
            
        res = []
        sorted_dic = dict(sorted(dic.items(), key = lambda x: x[1]))


        for i in sorted_dic:
            if not res:
                res.append(i)
            else:
                if dic[i] == dic[res[-1]]:
                    res.append(i)
                else:break

        return res
            
        


        