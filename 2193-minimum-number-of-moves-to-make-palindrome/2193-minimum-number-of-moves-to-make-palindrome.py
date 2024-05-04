
class Solution(object):
    def minMovesToMakePalindrome(self, s):
       
        s = list(s)
        result = 0
        while s:
            i = s.index(s[-1])
            if i == len(s)-1:
                result += i//2
            else:
                result += i
                s.pop(i)
            s.pop()
        return result