import collections
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
        if not root:
            return []
        result = []
        stack = collections.deque()
        stack.append(root)
        while stack:
            level = []
            n = len(stack)
            for _ in range(n):
                node = stack.popleft()
                level.append(node.val)
                if node.left: stack.append(node.left)
                if node.right:stack.append(node.right)
            result.append(level)
            if not stack:
                break
            level = []
            n = len(stack)
            for _ in range(n):
                node = stack.pop()
                level.append(node.val)
                if node.right:stack.appendleft(node.right)
                if node.left: stack.appendleft(node.left)
            result.append(level)
        return result
