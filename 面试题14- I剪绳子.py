class Solution(object):
    def __init__(self):
        self.dp = [0]*60
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        #时间：O(n2) 空间：O(n)
        # for i in range(1,n+1):
        #     for j in range(1,i//2+1):
        #         self.dp[i] = max(max(self.dp[i-j],i-j)*j,self.dp[i])
        # return self.dp[n]

        #时间O(n) 空间O(1)
        # dp = [0,0,1]
        # for i in range(3,n+1):
        #     dp[i%3] = max(max(dp[(i-1)%3],i-1),2*max(dp[(i-2)%3],i-2),3*max(dp[(i-3)%3],i-3))
        # return dp[n%3]

        #时间O(1) 空间O(1)
        if n<4:
            return max(0,n-1)
        a,b = n//3,n%3
        if b==0:
            return pow(3,a)
        elif b==1:
            return pow(3,a-1)*4
        elif b==2:
            return pow(3,a)*2

s = Solution()
print(s.cuttingRope(10))
