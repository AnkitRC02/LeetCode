class Solution(object):
    def minSwaps(self, nums):
        k = sum(nums)
        nums = nums * 2
        n = len(nums)
        
        max_ones_in_window = 0
        ones_in_window = sum(nums[:k])
        max_ones_in_window = ones_in_window
        
        for i in range(k, n):
            ones_in_window += nums[i] - nums[i - k]
            max_ones_in_window = max(max_ones_in_window, ones_in_window)
        
        return k - max_ones_in_window

        