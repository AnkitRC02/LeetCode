import itertools
class Solution(object):
    def minCost(self, nums, cost):
        def f(x):
            return sum(abs(y-x)*c for y, c in itertools.izip(nums, cost))
        def check(x, t):
            return sum(c for y, c in itertools.izip(nums, cost) if y <= x) >= t
        idxs = range(len(nums))
        idxs.sort(key=lambda x: nums[x])
        left, right = 0, len(idxs)-1
        total = sum(cost)
        median = (total+1)//2
        while left <= right:
            mid = left+(right-left)//2
            if check(nums[idxs[mid]], median):
                right = mid-1
            else:
                left = mid+1
        return f(nums[idxs[left]])