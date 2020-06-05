import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = collections.Counter(s)
        for i in range(len(s)):
            if p[s[i]] == 1:
                return s[i]
        return ' '

s = Solution()
print(s.firstUniqChar("abaccdeff"))
