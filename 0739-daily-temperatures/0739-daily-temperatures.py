class Solution(object):
    def dailyTemperatures(self, T):
        n = len(T)
        res = [0] * n # initialize an empty array

        for i in range(n - 2, -1, -1):
            k = i + 1

            while T[i] >= T[k] and res[k] > 0:
                print(i)
                k += res[k]

            if T[k] > T[i]:
                res[i] = k - i
        return res