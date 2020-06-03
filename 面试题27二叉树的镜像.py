# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # if root is None or (root.left is None and root.right is None):
        #     return root
        # newroot = TreeNode(root.val)
        # newroot.left = self.mirrorTree(root.right)
        # newroot.right = self.mirrorTree(root.left)
        # return newroot
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left,node.right = node.right,node.left
        return root
        
        