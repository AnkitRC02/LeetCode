class Solution:
    def reorganizeString(self, S: str) -> str:
        n = len(S)
        a= []
        
        for c,x in sorted((S.count(x), x) for x in set(S)):
            if c > (n+1)/2:
                return ''
            a.extend(c*x)
        ans = [None] * n
        ans[::2], ans[1::2] = a[n//2:], a[:n//2]
        return "".join(ans)
        
        
        