# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if not root:
        #     return 0
        # depth = 0
        # depth+=1
        # depth +=max(self.maxDepth(root.left),self.maxDepth(root.right))
        # return depth

        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            temp = []
            for node in queue:
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            queue = temp
            depth+=1
        return depth
