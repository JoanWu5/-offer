class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = 0
        vote = 0
        for num in nums:
            if count == 0:
                result = num  
            if num == result:
                count+=1
            else:
                count -=1
        for num in nums:
            if num == result:
                vote+=1
        return result if vote>len(nums)//2 else 0

s = Solution()
print(s.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))