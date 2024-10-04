import collections

class Solution(object):
    def dividePlayers(self, skill):

        target = sum(skill)//(len(skill)//2)
        cnt = collections.Counter(skill)
        result = 0
        for k, v in cnt.iteritems():
            if target-k not in cnt or cnt[target-k] != cnt[k]:
                return -1
            result += k*(target-k)*v
        return result//2
        