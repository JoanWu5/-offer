class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # s = s.strip().split()
        # result = []
        # for i in range(len(s)-1,-1,-1):
        #     if s[i] != ' ':
        #         result.append(s[i])
        # return ' '.join(result)

        result = []
        s = s.strip()
        i = j = len(s)-1
        while i>=0:
            while i>=0 and s[i]!=' ':
                i-=1
            result.append(s[i+1:j+1])
            while s[i]== ' ':
                i-=1
            j=i
        return ' '.join(result)

s = Solution()
print(s.reverseWords("a good   example"))