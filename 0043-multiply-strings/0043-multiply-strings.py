class Solution(object):
    def multiply(self, num1, num2):
        num1, num2 = num1[::-1], num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                res[i + j] += int(num1[i]) * int(num2[j])
                res[i + j + 1] += res[i + j] / 10
                res[i + j] %= 10
        i = len(res) - 1
        while i > 0 and res[i] == 0:
            i -= 1
        return ''.join(map(str, res[i::-1]))
class Solution2(object):
    def multiply(self, num1, num2):
        return str(int(num1) * int(num2))
if __name__ == "__main__":
    print Solution().multiply("123", "1000")