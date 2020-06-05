class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = [0]*32
        for num in nums:
            for j in range(32):
                counts[j] +=num&1
                num>>=1
        result = 0
        m = 3
        for i in range(32):
            result<<=1
            result+=counts[31-i]%m
        return result if counts[31]%m==0 else ~(result^0xffffffff)

    