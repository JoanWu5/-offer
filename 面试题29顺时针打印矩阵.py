class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None or len(matrix)==0 or matrix[0] is None or len(matrix[0])==0:
            return []
        result = []
        l = 0
        r = len(matrix[0])-1
        t = 0
        b = len(matrix)-1
        while True:
            for i in range(l,r+1):
                result.append(matrix[t][i])
            t+=1
            if t>b:break
            for i in range(t,b+1):
                result.append(matrix[i][r])
            r-=1
            if l>r:break
            for i in range(r,l-1,-1):
                result.append(matrix[b][i])
            b-=1
            if t>b:break
            for i in range(b,t-1,-1):
                result.append(matrix[i][l])
            l+=1
            if l>r:break
        return result


