from collections import deque
class Solution(object):
    def removeInvalidParentheses(self, s):
    
        def isValid(s):
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        ans = []
        lookup = {s:False}
        queue = deque([s])
        while len(queue) > 0:
            s = queue.popleft()
            if isValid(s):
                if lookup[s] == False:
                    ans.append(s)
                    lookup[s] = True
            elif len(ans) == 0:
    
                for i in range(len(s)):
                    if s[i] == "(" or s[i] == ")":
                      s2 = s[0:i]+s[i+1:]
                      if s2 not in lookup:
                        queue.append(s[0:i]+s[i+1:])
                        lookup[s2] = False
        return ans