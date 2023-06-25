class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [sys.maxint]*(n+1)
        res[0] = 0
        for i in range(1,n+1):
            j = 1
            while j*j <=i:
                res[i] = min(res[i-j*j]+1, res[i])
                j+=1
        return res[n]