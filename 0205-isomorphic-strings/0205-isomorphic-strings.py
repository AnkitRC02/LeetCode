class Solution:

    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
    
        return self.halfIsom(s, t) and self.halfIsom(t, s)

    def halfIsom(self, s, t):
        res = {}
        for i in xrange(len(s)):
            if s[i] not in res:
                res[s[i]] = t[i]
            elif res[s[i]] != t[i]:
                return False
        return True