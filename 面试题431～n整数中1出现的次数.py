class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
    # cur = 0 result+=high*digit
    # cur = 1 result+=high*digit+low+1
    # cur>1 result+=high*digit+digit
        digit = 1
        result = 0
        high,cur,low = n//10,n%10,0
        while high!=0 or cur!=0:
            if cur == 0: result+=high*digit
            elif cur == 1:result+=high*digit+low+1
            else: result+=(high+1)*digit
            low+=cur*digit
            cur = high%10
            high = high//10
            digit*=10
        return result

s = Solution()
print(s.countDigitOne(12))