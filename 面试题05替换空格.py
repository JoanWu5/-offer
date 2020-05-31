class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        #时间O(n)
        # s = list(s)
        # for i in range(len(s)):
        #     if s[i] == ' ':
        #         s[i] = '%20'
        # s = ''.join(s)
        # return s
        # return s.replace(' ','%20')

        #在原字符串上直接修改O(n)
        if len(s)<1:
            return ''
        num_blank = 0
        for i in range(len(s)):
            if s[i] == ' ':
                num_blank+=1
        s_len = len(s)
        new_len = s_len+num_blank*2
        for i in range(s_len,new_len):
            s+=' '
        p1 = s_len-1
        p2 = new_len-1
        while p1<p2 and p1>=0:
            if s[p1] == ' ':
                s = s[:p2]+'0'+s[p2+1:new_len]
                p2-=1
                s = s[:p2]+'2'+s[p2+1:new_len]
                p2-=1
                s = s[:p2]+'%'+s[p2+1:new_len]
                p2-=1
                p1-=1
            else:
                ch = s[p1]
                s = s[:p2]+ch+s[p2+1:new_len]
                p1-=1
                p2-=1
        return s

s = Solution()
print(s.replaceSpace('We are happy'))