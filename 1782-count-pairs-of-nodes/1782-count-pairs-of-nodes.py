
import collections
import itertools

class Solution(object):
    def countPairs(self, n, edges, queries):
        degree = [0]*(n+1)
        shared = collections.Counter((min(n1, n2), max(n1, n2)) for n1, n2 in edges)
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
        cnt = [0]*(2*(max(degree[1:])+1))
        count = collections.Counter(degree[1:])
        for i, j in itertools.product(count, count):  # Time: O(d^2) = O(e)
            if i < j:
                cnt[i+j] += count[i]*count[j]
            elif i == j:
                cnt[i+j] += count[i]*(count[i]-1)//2
        for (i, j), shared_degree in shared.iteritems():
            cnt[degree[i]+degree[j]] -= 1
            cnt[degree[i]+degree[j]-shared_degree] += 1
        for i in reversed(xrange(len(cnt)-1)):  # accumulate
            cnt[i] += cnt[i+1]
        return [cnt[q+1] if q+1 < len(cnt) else 0 for q in queries]

