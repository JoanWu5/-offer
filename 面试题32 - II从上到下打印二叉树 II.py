# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        stack = [root]
        while True:
            level = []
            n = len(stack)
            for _ in range(n):
                node = stack.pop(0)
                level.append(node.val)
                if node.left:stack.append(node.left)
                if node.right:stack.append(node.right)
            if level==[]:
                break
            else:
                result.append(level)
        return result