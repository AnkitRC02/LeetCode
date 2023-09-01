class Solution:
 def countBits(self, n: int) -> List[int]:
  results = [0] * (n + 1)
 
  for i in range(1, n + 1):
   j = i
   while j != 0:
    if j % 2 == 1:
     results[i] += 1
    j = j // 2
 
  return results