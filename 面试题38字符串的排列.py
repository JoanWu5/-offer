import collections
class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        visited = collections.Counter(s)
        result  = []
        self.helper(s,visited,'',result)
        return result

    def helper(self,s,visited,path,result):
        if len(path) == len(s):
            result.append(path)
            return
        for i in visited:
            if visited[i]>0:
                visited[i]-=1
                self.helper(s,visited,path+i,result)
                visited[i]+=1