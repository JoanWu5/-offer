# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.helper(root,root)

    def helper(self,node1,node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False
        else:
            if node1.val == node2.val:
                return self.helper(node1.left,node2.right) and self.helper(node1.right,node2.left)
            else:
                return False
