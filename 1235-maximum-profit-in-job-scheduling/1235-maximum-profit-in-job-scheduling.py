
import itertools
import bisect

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(itertools.izip(endTime, startTime, profit))
        dp = [(0, 0)]
        for e, s, p in jobs:
            i = bisect.bisect_right(dp, (s+1, 0))-1
            if dp[i][1]+p > dp[-1][1]:
                dp.append((e, dp[i][1]+p))
        return dp[-1][1]
