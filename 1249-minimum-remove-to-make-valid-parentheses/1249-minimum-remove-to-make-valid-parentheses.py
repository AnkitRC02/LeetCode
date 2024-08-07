class Solution(object):
    def minRemoveToMakeValid(self, s):
        result = list(s)
        count = 0
        for i, v in enumerate(result):
            if v == '(':
                count += 1
            elif v == ')':
                if count:
                    count -= 1
                else:
                    result[i] = ""
        if count:
            for i in reversed(xrange(len(result))):
                if result[i] == '(':
                    result[i] = ""
                    count -= 1
                    if not count:
                        break
        return "".join(result)