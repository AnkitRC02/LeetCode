class Solution(object):
    def maxUniqueSplit(self, s):
        def popcount(n):
            count = 0
            while n:
                n &= n-1
                count += 1
            return count
    
        result = 1
        total = 2**(len(s)-1)
        mask = 0
        while mask < total:
            if popcount(mask) < result:
                mask += 1
                continue
            lookup, curr, base = set(), [], total//2
            for i in xrange(len(s)):
                curr.append(s[i])
                if (mask&base) or base == 0:
                    if "".join(curr) in lookup:
                        mask = (mask | (base-1)) + 1 if base else mask+1 
                        break
                    lookup.add("".join(curr))
                    curr = []
                base >>= 1
            else:
                result = max(result, len(lookup))
                mask += 1
        return result