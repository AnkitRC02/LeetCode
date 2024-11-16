class Solution(object):
    def resultsArray(self, nums, k):
        return [nums[i+k-1] if all(nums[j]+1 == nums[j+1] for j in xrange(i, i+k-1)) else -1 for i in xrange(len(nums)-k+1)]