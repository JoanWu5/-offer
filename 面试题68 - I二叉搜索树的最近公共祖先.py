# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #迭代
        # if root.val<p.val and root.val<q.val:
        #     return self.lowestCommonAncestor(root.right,p,q)
        # elif root.val>p.val and root.val>q.val:
        #     return self.lowestCommonAncestor(root.left,p,q)
        # else:
        #     return root

        #非迭代
        while root:
            if root.val<p.val and root.val<q.val:
                root = root.right
            elif root.val>p.val and root.val>q.val:
                root = root.left
            else:
                break
        return root