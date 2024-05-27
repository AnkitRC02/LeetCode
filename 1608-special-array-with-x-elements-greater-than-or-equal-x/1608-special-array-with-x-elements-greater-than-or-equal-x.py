
class Solution(object):
    def specialArray(self, nums):
        MAX_NUM = 1000
        count = [0]*(MAX_NUM+1)
        for num in nums:
            count[num] += 1
        n = len(nums)
        for i in xrange(len(count)):
            if i == n:
                return i
            n -= count[i]
        return -1