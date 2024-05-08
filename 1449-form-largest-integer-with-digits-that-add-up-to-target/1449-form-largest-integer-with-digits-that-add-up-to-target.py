

class Solution(object):
    def largestNumber(self, cost, target):
        dp = [0]
        for t in xrange(1, target+1):
            dp.append(-1)
            for i, c in enumerate(cost):
                if t-c < 0 or dp[t-c] < 0:
                    continue
                dp[t] = max(dp[t], dp[t-c]+1)
        if dp[target] < 0:
            return "0"
        result = []
        for i in reversed(xrange(9)):
            while target >= cost[i] and dp[target] == dp[target-cost[i]]+1:
                target -= cost[i]
                result.append(i+1)
        return "".join(map(str, result))
