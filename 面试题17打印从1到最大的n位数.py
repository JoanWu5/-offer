class Solution(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # return list(range(1,pow(10,n)))

        #大数情况
        number = ['']*n
        result = []
        for i in range(10):
            number[0] = str(i)
            self.helper(number,n,0,result)
        return result
    
    def helper(self,number,n,index,result):
        if index == n-1:
            begin0 = True
            xx = ''
            for i in range(n):
                if begin0 and int(number[i])!=0:
                    begin0 = False
                if not begin0:
                    xx+=number[i]
            if xx!='':
                result.append(int(xx))
            return
        for i in range(10):
            number[index+1] = str(i)
            self.helper(number,n,index+1,result)


s = Solution()
print(s.printNumbers(2))