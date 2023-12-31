class Solution(object):
    def fullJustify(self, words, maxWidth):
        def addSpaces(i, spaceCnt, maxWidth, is_last):
            if i < spaceCnt:
                return 1 if is_last else (maxWidth // spaceCnt) + int(i < maxWidth % spaceCnt)
            return 0

        def connect(words, maxWidth, begin, end, length, is_last):
            s = []
            n = end - begin
            for i in xrange(n):
                s += words[begin + i],
                s += ' ' * addSpaces(i, n - 1, maxWidth - length, is_last),
            line = "".join(s)
            if len(line) < maxWidth:
                line += ' ' * (maxWidth - len(line))
            return line

        res = []
        begin, length = 0, 0
        for i in xrange(len(words)):
            if length + len(words[i]) + (i - begin) > maxWidth:
                res += connect(words, maxWidth, begin, i, length, False),
                begin, length = i, 0
            length += len(words[i])

        res += connect(words, maxWidth, begin, len(words), length, True),
        return res

