class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #时间优先：时间O(n) 空间O(n)
        # d = {}
        # for num in nums:
        #     if num in d:
        #         return num
        #     else:
        #         d[num] =1

        #空间优先：时间O(nlogn) 空间O(1)
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]

        #空间优先O(1)且不修改原数组 时间O(n)
        # for i in range(len(nums)):
        #     while i!=nums[i]:
        #         if nums[i]==nums[nums[i]]:
        #             return nums[i]
        #         else:
        #             temp = nums[i]
        #             nums[i],nums[temp]=nums[temp],nums[i]

        #针对所有数字在1~n范围内的长度为n+1的数组:[0, 1, 2, 0, 4, 5, 6, 7, 8, 9]不成立
        def countRange(nums,start,end):
            count = 0
            for i in range(len(nums)):
                if start<=nums[i]<=end:
                    count+=1
            return count
        start = 1
        end = len(nums)-1
        while start<=end:
            mid = (end-start)//2+start
            count = countRange(nums,start,mid)
            print(count)
            if start==end:
                if count>1:
                    return start
                else:
                    break
            if count>mid-start+1:
                end = mid
            else:
                start = mid+1
            print(start,mid,end)
        return -1
        

s = Solution()
print(s.findRepeatNumber([0, 1, 2, 0, 4, 5, 6, 7, 8, 9]))