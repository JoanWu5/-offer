class Solution(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        #其中dp（N,S）表示投第N个骰子时，点数和为S的次数
        dp = [[0]*(6*n+1) for _ in range(n+1)]
        for i in range(1,7):
            dp[1][i] = 1
        for i in range(2,n+1):
            for j in range(i,i*6+1):
                for k in range(1,7):
                    if j>=k+1:
                        dp[i][j]+=dp[i-1][j-k]
        result = []
        for i in range(n,6*n+1):
            result.append(dp[n][i]*1.0/6**n)
        return result

s = Solution()
print(s.twoSum(2))