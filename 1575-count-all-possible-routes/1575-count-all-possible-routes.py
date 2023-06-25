import bisect
class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        MOD = 10**9+7
        s, f = locations[start], locations[finish];
        locations.sort()
        start, finish = bisect.bisect_left(locations, s), bisect.bisect_left(locations, f)
        left = [[0]*(fuel+1) for _ in xrange(len(locations))]
        right = [[0]*(fuel+1) for _ in xrange(len(locations))]
        for f in xrange(1, fuel+1):
            for j in xrange(len(locations)-1):
                d = locations[j+1]-locations[j]
                if f > d:
                    left[j][f] = (right[j+1][f-d] + 2*left[j+1][f-d] % MOD) % MOD;
                elif f == d:
                    left[j][f] = int(j+1 == start)
            for j in xrange(1, len(locations)):
                d = locations[j]-locations[j-1]
                if f > d:
                    right[j][f] = (left[j-1][f-d] + 2*right[j-1][f-d] % MOD) % MOD
                elif f == d:
                    right[j][f] = int(j-1 == start)
        result = int(start == finish)
        for f in xrange(1, fuel+1):
            result = ((result + left[finish][f]) % MOD + right[finish][f]) % MOD
        return result