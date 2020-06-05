class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        while left<right:
            if nums[left]+nums[right]==target:
                return [nums[left],nums[right]]
            elif nums[left]+nums[right]>target:
                right-=1
            else:
                left+=1
        