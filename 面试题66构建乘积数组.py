class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        p = 1
        result = [1]*len(a)
        for i in range(len(a)):
            result[i]*=p
            p*=a[i]
        p = 1
        for i in range(len(a)-1,-1,-1):
            result[i]*=p
            p*=a[i]
        return result

s = Solution()
print(s.constructArr([1,2,3,4,5]))