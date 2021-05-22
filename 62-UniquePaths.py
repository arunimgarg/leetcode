# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        matrix = [[1] * m] * n

        for i in range(1,n):
            for j in range(1,m):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        return matrix[n-1][m-1]
