class Solution:
    def matrixBlockSum(self, mat,k):
        m = len(mat)
        n = len(mat[0])
        lst = [[0]*n for _ in range(m)]
        for i in range(m):
            value = 0
            for j in range(n):
                value += mat[i][j]
                lst[i][j] = value
        retM = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                lr = max(0, i-k)
                hr = min(m-1, i+k)
                ps = 0
                for r in range(lr, hr+1):
                    hc = min(n-1, j+k)
                    lc = j - k - 1
                    if lc < 0:
                        ps += lst[r][hc]
                    else:
                        ps += lst[r][hc] - lst[r][lc]
                retM[i][j] = ps
        return retM
