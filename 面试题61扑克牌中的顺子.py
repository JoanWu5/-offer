class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<5:
            return False
        nums.sort()
        count = 0
        gap = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count+=1
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                if nums[i]==nums[i-1]:
                    return False
                gap+=nums[i]-nums[i-1]-1
        if count>=gap:
            return True
        else:
            return False
    
s = Solution()
print(s.isStraight([0,0,8,5,4]))