class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str == '':
            return 0
        flag = 0
        if str[0] in ['-','+']:
            flag = 1
        if flag and len(str)==1:
            return 0
        if flag+1<len(str) and not str[flag].isdigit():
            return 0
        result = 0
        for i in range(flag,len(str)):
            if str[i].isdigit():
                result = 10*result+int(str[i])
            else:
                break
        if flag and str[0]=='-':
            result = -result
        return max(min(result,pow(2,31)-1),-pow(2,31))

s = Solution()
print(s.strToInt( "3.14"))
        
        