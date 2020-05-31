class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #时间O(m+n)
        if matrix == None or len(matrix)==0 or matrix[0] == None or len(matrix[0])==0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        i = m-1
        j = 0
        while i>=0 and i<m and j>=0 and j<n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j]<target:
                j+=1
            else:
                i-=1
        return False

s = Solution()
print(s.findNumberIn2DArray([],20))
                