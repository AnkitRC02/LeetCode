class Solution(object):
    def minimizeMax(self, nums, p):
        def check(x):
            i = cnt = 0
            while i+1 < len(nums) and cnt < p:
                if nums[i+1]-nums[i] <= x:
                    i += 1
                    cnt += 1
                i += 1
            return cnt == p

        nums.sort()
        left, right = 0, nums[-1]-nums[0]
        while left <= right:
            mid = left + (right-left)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return left