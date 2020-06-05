class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (right-left)//2+left
            if mid!=nums[mid]:
                if mid == 0 or mid-1 == nums[mid-1]:
                    return mid
                right = mid-1
            else:
                left = mid+1
        if left == len(nums):
            return left

s = Solution()
print(s.missingNumber( [0,1,2,3,4,5,6,7,9]))