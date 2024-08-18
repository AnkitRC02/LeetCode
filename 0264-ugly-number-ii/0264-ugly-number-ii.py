class Solution(object):
    def nthUglyNumber(self, n):
        ugly = [1] * n
        i2 = i3 = i5 = 0
        next_2, next_3, next_5 = 2, 3, 5
        for i in range(1, n):
            ugly[i] = min(next_2, next_3, next_5)
            if ugly[i] == next_2:
                i2 += 1
                next_2 = ugly[i2] * 2
            if ugly[i] == next_3:
                i3 += 1
                next_3 = ugly[i3] * 3
            if ugly[i] == next_5:
                i5 += 1
                next_5 = ugly[i5] * 5
        return ugly[-1]
        