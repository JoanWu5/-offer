class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        temp = [0]*n
        return self.mergeSort(nums,temp,0,n-1)
    
    def mergeSort(self,nums,temp,left,right):
        if left>=right:
            return 0
        mid = (right-left)//2+left
        count = self.mergeSort(nums,temp,left,mid)+self.mergeSort(nums,temp,mid+1,right)
        i,j,pos = left,mid+1,left
        while i<=mid and j<=right:
            if nums[i]<=nums[j]:
                temp[pos] = nums[i]
                i+=1
                count+=j-mid-1
            else:
                temp[pos] = nums[j]
                j+=1
            pos+=1
        for k in range(i,mid+1):
            temp[pos] = nums[k]
            count+=j-mid-1
            pos+=1
        for k in range(j,right+1):
            temp[pos] = nums[k]
            pos+=1
        nums[left:right+1] = temp[left:right+1]
        return count

s = Solution()
print(s.reversePairs([7,5,6,4]))
