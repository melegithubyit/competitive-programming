import heapq
class Solution:
    def largestInteger(self, num: int) -> int:
        number = str(num)
        output = ''
        opq, epq = [], []
        for i in number:
            if int(i) % 2 == 0:
                epq.append(int(i))
            else:
                opq.append(int(i))

        for i in number:
            if int(i) % 2 == 0:
                heapq._heapify_max(epq)
                val = epq.pop(0)
                output += str(val)

            else:
                heapq._heapify_max(opq)
                val = opq.pop(0)
                output += str(val)

        return int(output)
