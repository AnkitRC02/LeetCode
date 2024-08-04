class Solution(object):
    def rangeSum(self, nums, n, left, right):
        mod = 10**9 + 7
        sub_sums = []
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                sub_sums.append(curr_sum)
        sub_sums.sort()
        return sum(sub_sums[left-1:right]) % mod

        