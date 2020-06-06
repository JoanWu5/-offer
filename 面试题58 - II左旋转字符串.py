class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        return s[n:len(s)]+s[:n]

s = Solution()
print(s.reverseLeftWords(s = "abcdefg", n = 2))