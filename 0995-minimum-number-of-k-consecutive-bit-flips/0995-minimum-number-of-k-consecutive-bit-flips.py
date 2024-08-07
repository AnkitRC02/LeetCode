class Solution(object):
    def minKBitFlips(self, A, K):
        n = len(A)
        flip = [0 for _ in range(n)]
        flip_cnt = 0
        for i in range(n):
            if (A[i] + flip_cnt) % 2 == 0:
                if i + K <= n:
                    flip[i] = 1
                    flip_cnt += 1
                else:
                    return -1
            if i >= K - 1 and flip[i - K + 1]:
                flip_cnt -= 1
        return sum(flip)