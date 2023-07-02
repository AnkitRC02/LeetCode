import itertools
class Solution(object):
    def maximumRequests(self, n, requests):
        for k in reversed(xrange(1, len(requests)+1)):
            for c in itertools.combinations(xrange(len(requests)), k):
                change = [0]*n
                for i in c:
                    change[requests[i][0]] -= 1
                    change[requests[i][1]] += 1
                if all(c == 0 for c in change):
                    return k
        return 0        