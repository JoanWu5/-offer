class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        left = 0
        right = len(numbers)-1
        while left<right:
            mid = (right-left)//2 + left
            if numbers[mid]>numbers[right]:
                left = mid+1
            elif numbers[mid]<numbers[left]:
                right = mid
            else:
                right-=1
        return numbers[left]


s = Solution()
print(s.minArray([2,2,2,0,1]))