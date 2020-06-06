class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        x = 0xFFFFFFFF
        a,b = a&x,b&x
        while b!=0:
            a,b = (a^b)&x,((a&b)<<1)&x
        return a if a <=0x7FFFFFFF else ~(a^x)

s = Solution()
print(s.add(1,-2))
