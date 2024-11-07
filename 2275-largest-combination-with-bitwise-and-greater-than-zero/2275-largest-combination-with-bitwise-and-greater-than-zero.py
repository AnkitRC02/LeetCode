class Solution(object):
    def largestCombination(self, candidates):
        cnt = []
        base, mx = 1, max(candidates)
        while base <= mx:
            cnt.append(sum(x&base > 0 for x in candidates))
            base <<= 1
        return max(cnt)