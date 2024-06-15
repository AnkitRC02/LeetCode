import heapq

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        if k == 0:
            return w
        
        min_heap = []
        for c, p in zip(capital, profits):
            heapq.heappush(min_heap, (c, p))
        
        max_heap = []
        
        for _ in range(k):
            while min_heap and min_heap[0][0] <= w:
                c, p = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (-p, c))
            
            if not max_heap:
                break
            
            w -= heapq.heappop(max_heap)[0]
        
        return w