class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        count = 0
        while left<=right:
            mid = (right-left)//2+left
            if nums[mid] == target:
                temp = mid
                count+=1
                while mid+1<=len(nums)-1 and nums[mid]==nums[mid+1]:
                    mid+=1
                    count+=1
                while temp-1>=0 and nums[temp] ==nums[temp-1]:
                    temp-=1
                    count+=1
                break
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
        return count

s = Solution()
print(s.search([1],1))