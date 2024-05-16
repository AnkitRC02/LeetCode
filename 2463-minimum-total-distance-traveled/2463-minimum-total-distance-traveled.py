import collections

class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        robot.sort(), factory.sort()
        dp = [float("inf")]*(len(robot)+1) 
        dp[0] = 0
        for i in xrange(len(factory)):
            for j in reversed(xrange(1, len(robot)+1)):
                curr = 0
                for k in xrange(min(factory[i][1], j)+1):
                    dp[j] = min(dp[j], dp[j-k]+curr)
                    if (j-1)-k >= 0:
                        curr += abs(robot[(j-1)-k]-factory[i][0])
        return dp[-1]