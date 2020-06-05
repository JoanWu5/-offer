class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        result = 0
        i =-1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(i,dic[s[j]])
            dic[s[j]] = j
            result = max(result,j-i)
        return result

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))