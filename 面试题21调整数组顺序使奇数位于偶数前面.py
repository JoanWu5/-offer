class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        while left<right:
            while left<right and nums[left]&1:
                left+=1
            while left<right and not nums[right]&1:
                right-=1
            if left<right:
                nums[left],nums[right] = nums[right],nums[left]
            left+=1
            right-=1
        return nums

s = Solution()
print(s.exchange([1,2,3,4]))
