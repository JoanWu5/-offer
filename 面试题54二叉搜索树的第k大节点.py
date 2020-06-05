# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def dfs(root,k):
            if not root:
                return
            dfs(root.right)
            if self.k==0: return
            self.k-=1
            if self.k==0: 
                self.result = root.val
                return
            dfs(root.left)
        self.k = k
        dfs(root)
        return self.result
