class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()
        n = len(nums)
        
        def count_pairs_with_distance_less_than_or_equal(mid):
            count = 0
            left = 0
            for right in range(n):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count
        
        low, high = 0, nums[-1] - nums[0]
        
        while low < high:
            mid = (low + high) // 2
            if count_pairs_with_distance_less_than_or_equal(mid) >= k:
                high = mid
            else:
                low = mid + 1
        
        return low
        