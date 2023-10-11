class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if not clips:
            return 0
        start,count,maxEnd = 0, 0, 0 
        n = len(clips)
        k = -1
        while(start < T and k != start):
            k = start
            maxEnd = 0
            for i in range(0,n):
                if(clips[i][0] <= start):
                    maxEnd = max(maxEnd,clips[i][1])
            start = maxEnd
            count += 1
        if(k == start):
            return -1
        return count