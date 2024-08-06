import collections
class Solution(object):
    def minimumPushes(self, word):
        return sum(x*(i//(9-2+1)+1) for i, x in enumerate(sorted(collections.Counter(word).itervalues(), reverse=True)))
        