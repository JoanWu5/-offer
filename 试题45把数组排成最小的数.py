import functools
class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def sort_rule(x,y):
            a,b = x+y,y+x
            if a>b:return 1
            elif a<b:return -1
            else: return 0
        strs = [str(num) for num in nums]
        strs.sort(key=functools.cmp_to_key(sort_rule))
        return ''.join(strs)

s = Solution()
print(s.minNumber([3,30,34,5,9]))