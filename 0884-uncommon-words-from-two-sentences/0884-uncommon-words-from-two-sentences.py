class Solution:
    def uncommonFromSentences(self, A: 'str', B: 'str') -> 'List[str]':
        s = A + ' '+B
        s = s.split()
        ans = []
        for word in set(s):
            if s.count(word)==1:
                ans.append(word)
        return ans
