
class Solution(object):
    def minimumDistance(self, word):
        def distance(a, b):
            return abs(a//6 - b//6) + abs(a%6 - b%6)

        dp = [0]*26
        for i in xrange(len(word)-1):
            b, c = ord(word[i])-ord('A'), ord(word[i+1])-ord('A')
            dp[b] = max(dp[a] - distance(a, c) + distance(b, c) for a in xrange(26))
        return sum(distance(ord(word[i])-ord('A'), ord(word[i+1])-ord('A')) for i in xrange(len(word)-1)) - max(dp)
