from queue import Queue
class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        #O(mn)
        # visited = set([(0,0)])
        # for i in range(m):
        #     for j in range(n):
        #         if ((i-1,j) in visited or (i,j-1) in visited) and self.sumDigit(i)+self.sumDigit(j)<=k:
        #             visited.add((i,j))
        # return len(visited)
        q = Queue()
        q.put((0,0))
        visited = set()
        while not q.empty():
            x,y = q.get()
            if (x,y) not in visited and 0<=x<m and 0<=y<n and self.sumDigit(x)+self.sumDigit(y)<=k:
                visited.add((x,y))
                for nx,ny in [(x+1,y),(x,y+1)]:
                    q.put((nx,ny))
        return len(visited)

    def sumDigit(self,number):
        result = 0
        while number:
            result+=number%10
            number = number//10  
        return result        

s =Solution()
print(s.movingCount(16,8,4))