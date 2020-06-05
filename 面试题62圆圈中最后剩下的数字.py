class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # f = 0
        # for i in range(2,n+1):
        #     f = (m+f)%i
        # return f
        def f(n,m):
            if n==0:
                return 0
            x = f(n-1,m)
            return (x+m)%n
        return f(n,m)