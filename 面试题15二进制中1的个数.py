class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #时间O(log2n) 空间O(1) 没办法解决负数的问题
        # result = 0
        # while n:
        #     if n&1:
        #         result+=1
        #     n = n>>1
        # return result

        #解决负数的问题
        # result = 0
        # flag = 1
        # while abs(n)>=abs(flag):
        #     if n&flag:
        #         result+=1
        #     flag = flag<<1
        # return result

        #时间：O(M) M为n中1的个数 空间O(1)
        #n&(n−1) 解析： 二进制数字 n最右边的 1变成 0 ，其余不变。
        result = 0
        n = abs(n)
        while n:
            result+=1
            n = n&(n-1)
        return result

s = Solution()
print(s.hammingWeight(4))
