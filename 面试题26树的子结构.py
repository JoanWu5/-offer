# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        result = False
        if A and B:
            if A.val == B.val:
                result = self.helper(A,B)
            if not result:
                result = self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)
        return result

    def helper(self,A,B):
        if B is None:
            return True
        if A is None:
            return False
        if A.val != B.val:
            return False
        return self.helper(A.left,B.left) and self.helper(A.right,B.right)
        
