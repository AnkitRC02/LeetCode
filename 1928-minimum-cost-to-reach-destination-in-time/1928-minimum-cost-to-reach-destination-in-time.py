import collections
import heapq

class Solution(object):
    def minCost(self, maxTime, edges, passingFees):     
        adj = [[] for i in xrange(len(passingFees))]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        best = collections.defaultdict(lambda:float("inf"))
        best[0] = 0
        min_heap = [(passingFees[0], 0, 0)]
        while min_heap:
            result, u, w = heapq.heappop(min_heap)
            if w > maxTime:  
                continue
            if u == len(passingFees)-1:
                return result
            for v, nw in adj[u]:
                if w+nw < best[v]:
                    best[v] = w+nw
                    heapq.heappush(min_heap, (result+passingFees[v], v, w+nw))
        return -1