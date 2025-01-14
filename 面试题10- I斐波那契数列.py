class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        dp = [0]*3
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dp[2] = (dp[0]+dp[1])% 1000000007
            dp[0] = dp[1]
            dp[1] = dp[2]
        return dp[2] % 1000000007

s = Solution()
print(s.fib(5))