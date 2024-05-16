
class Solution(object):
    def waysToReachTarget(self, target, types):
        MOD = 10**9+7
        dp = [0]*(target+1)
        dp[0] = 1
        for c, m in types:
            for i in reversed(xrange(1, target+1)):
                for j in xrange(1, min(i//m, c)+1):
                    dp[i] = (dp[i]+dp[i-j*m])%MOD
        return dp[-1]
