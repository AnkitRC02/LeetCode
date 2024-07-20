class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        matrix = [[0]*len(colSum) for _ in xrange(len(rowSum))]
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                matrix[i][j] = min(rowSum[i], colSum[j]) 
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]
        return matrix
        