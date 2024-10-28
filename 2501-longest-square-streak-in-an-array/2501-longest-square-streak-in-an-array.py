class Solution(object):
    def longestSquareStreak(self, nums):
        sorted_nums = sorted(set(nums))
        squares = {x for x in sorted_nums if x%2 < 2}
        result = 0
        for x in sorted_nums:
            square, cnt = x**2, 1
            while square in squares:
                squares.remove(square)
                cnt += 1
                square *= square
            result = max(result, cnt)
        return result if result != 1 else -1

