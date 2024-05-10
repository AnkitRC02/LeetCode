
class Solution(object):
    def recoverArray(self, n, sums):
        sums.sort()  
        shift, l = 0, len(sums)
        result = []
        for _ in xrange(n):
            new_shift = sums[0]-sums[1]
            assert(new_shift <= 0)
            has_zero, j, k = False, 0, 0
            for i in xrange(l):
                if k < j and sums[k] == sums[i]:  
                    k += 1
                else:
                    if shift == sums[i]-new_shift:
                        has_zero = True
                    sums[j] = sums[i]-new_shift
                    j += 1
            if has_zero:  
                result.append(new_shift)
            else:  
                result.append(-new_shift)
                shift -= new_shift
            l //= 2
        return result
