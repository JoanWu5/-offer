class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        f = [[False]*(n+1) for i in range(m+1)]
        f[0][0] = True
        for i in range(m+1):
            for j in range(1,n+1):
                if p[j-1]!='*':
                    if i>0 and (s[i-1] == p[j-1] or p[j-1]=='.'):
                        f[i][j] = f[i-1][j-1]
                else:
                    if j>=2:
                        f[i][j] |= f[i][j-2]
                    if i>=1 and j>=2 and (s[i-1] == p[j-2] or p[j-2]=='.'):
                        f[i][j] |= f[i-1][j]
        return f[m][n]

s =Solution()
print(s.isMatch("","."))