import collections

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for word in dictionary:
            reduce(dict.__getitem__, word, trie).setdefault("_end")

        def replace(word):
            curr = trie
            for i, c in enumerate(word):
                if c not in curr:
                    break
                curr = curr[c]
                if "_end" in curr:
                    return word[:i+1]
            return word

        return " ".join(map(replace, sentence.split()))