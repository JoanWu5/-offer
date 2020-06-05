class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        dp = [0]*(len(num)+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1,len(num)):
            if '10'<=num[i-1:i+1]<='25':
                dp[i+1] = dp[i]+dp[i-1]
            else:
                dp[i+1]=dp[i]
        return dp[-1]