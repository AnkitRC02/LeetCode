class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_n = len(nums)
        res = len_n
        
        for i in range(len_n):
            res += i-nums[i]
            
        return res
        