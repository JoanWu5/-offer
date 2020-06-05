class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        if target<3:
            return
        left = 1
        right = 2
        result = []
        count = 3
        while left<=target//2:
            if count<target:
                right+=1
                count+=right
            elif count>target:
                count-=left
                left+=1
            else:
                result.append(list(range(left,right+1)))
                count-=left
                left+=1
        return result

s = Solution()
print(s.findContinuousSequence(15))
