import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deque = collections.deque()
        result = []
        n = len(nums)
        for i,j in zip(range(1-k,n+1-k),range(n)):
            if i>0 and deque[0] == nums[i-1]:
                deque.popleft()
            while deque and deque[-1]<nums[j]:
                deque.pop()
            deque.append(nums[j])
            if i>=0: result.append(deque[0])
        return result

s = Solution()
print(s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))