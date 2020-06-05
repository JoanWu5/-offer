class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j] = grid[0][0]
                elif i==0 and j>0:
                    dp[i][j] = max(0,dp[i][j-1])+grid[i][j]
                elif i>0 and j==0:
                    dp[i][j] = max(0,dp[i-1][j])+grid[i][j]
                else:
                    dp[i][j] = max(0,dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[-1][-1]