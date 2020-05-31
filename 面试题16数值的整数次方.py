class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        flag = 0
        if n <0:
            n = abs(n)
            flag = 1
        result = 1
        while n:
            if n&1:
                result*=x
            x = x*x
            n = n>>1
        if flag:
            result = 1/result
        return result

s = Solution()
print(s.myPow(0.44528,2))