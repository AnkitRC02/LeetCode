class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    sMap = defaultdict(list)

    for s in strs:
      sorted_s = "".join(sorted(s))
      sMap[sorted_s].append(s)
    
    return list(sMap.values())
        