class Solution:
  def minGroups(self, intervals: list[list[int]]) -> int:
    minHeap = []  

    for left, right in sorted(intervals):
      if minHeap and left > minHeap[0]:
        heapq.heappop(minHeap)
      heapq.heappush(minHeap, right)

    return len(minHeap)