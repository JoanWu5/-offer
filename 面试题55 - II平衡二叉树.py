# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #O(nlogn)
    #     if not root:
    #         return True
    #     if root:
    #         if abs(self.maxDepth(root.left)-self.maxDepth(root.right)>1:
    #             return False
    #         else:
    #             return self.isBalanced(root.left) and self.isBalanced(root.right)
                
    # def maxDepth(self,root):
    #     if not root:
    #         return 0
    #     return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
        
        #O(n)
        def recur(root):
            if not root:
                return 0
            left = recur(root.left)
            if left == -1:return -1
            right = recur(root.right)
            if right == -1: return -1
            return max(left,right)+1 if abs(left-right)<=1 else -1
        return recur(root)!=-1