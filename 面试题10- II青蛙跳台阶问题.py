class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        dp = [1]*3
        for i in range(2,n+1):
            dp[2] = (dp[0]+dp[1])%1000000007
            dp[0] = dp[1]
            dp[1] = dp[2]
        return dp[2]%1000000007

s = Solution()
print(s.numWays(7))