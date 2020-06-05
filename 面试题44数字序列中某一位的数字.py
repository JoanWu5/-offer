class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=9:
            return n
        digit = 1
        start = 1
        count = 9
        while n>count:
            n-=count
            start*=10
            digit+=1
            count = 9*start*digit
        num = start+(n-1)//digit
        return int(str(num)[(n-1)%digit])