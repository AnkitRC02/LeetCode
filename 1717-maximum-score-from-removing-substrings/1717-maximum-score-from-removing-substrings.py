class Solution:
    def maximumGain(self, s, x, y):
        def removeAndScore(s, first, second, points):
            stack = []
            score = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score

        if x > y:
            s, score1 = removeAndScore(s, 'a', 'b', x)
            _, score2 = removeAndScore(s, 'b', 'a', y)
        else:
            s, score1 = removeAndScore(s, 'b', 'a', y)
            _, score2 = removeAndScore(s, 'a', 'b', x)

        return score1 + score2
        