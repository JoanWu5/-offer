class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #时间O(n) 空间O(1)
        xor = 0
        num1 = 0
        num2 = 0
        for num in nums:
            xor^=num
        mask = 1
        while xor & mask == 0:
            mask = mask<<1
        for num in nums:
            if num&mask == 0:
                num1^=num
            else:
                num2^=num
        return [num1,num2]
s = Solution()
print(s.singleNumbers([4,1,4,6]))