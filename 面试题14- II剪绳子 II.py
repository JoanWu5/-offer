class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<4:
            return max(0,n-1)
        dp = [0]*3
        for i in range(4,n+1):
            dp[(i%3)] = max(max(dp[(i-1)%3],i-1),2*max(dp[(i-2)%3],i-2),3*max(dp[(i-3)%3],i-3))
        return dp[n%3]%1000000007

        