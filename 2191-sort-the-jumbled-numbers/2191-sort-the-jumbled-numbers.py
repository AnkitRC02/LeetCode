class Solution(object):
    def sortJumbled(self, mapping, nums):
        def map_value(num):
            return int(''.join(str(mapping[int(digit)]) for digit in str(num)))
        
        return sorted(nums, key=map_value)

        