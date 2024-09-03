class Solution(object):
    def getLucky(self, s, k):
        num = ''.join(str(ord(c) - ord('a') + 1) for c in s)
        for _ in range(k):
            num = str(sum(int(d) for d in num))
        return int(num)
