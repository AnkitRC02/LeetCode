import collections
import heapq

try:
    xrange          
except NameError:
    xrange = range  


class Solution(object):
    def isNStraightHand(self, hand, W):
        if len(hand) % W:
            return False

        counts = collections.defaultdict(int)
        for i in hand:
            counts[i] += 1

        min_heap = hand[:]
        heapq.heapify(min_heap)
        for _ in xrange(len(min_heap)//W):
            while counts[min_heap[0]] == 0:
                heapq.heappop(min_heap)
            start = heapq.heappop(min_heap)
            for _ in xrange(W):
                counts[start] -= 1
                if counts[start] < 0:
                    return False
                start += 1
        return True