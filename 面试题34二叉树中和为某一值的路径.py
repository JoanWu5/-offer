# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        self.helper(root,target,path,result)
        return result

    def helper(self,node,target,path,result):
        if not node:
            return
        if target == node.val and node.left is None and node.right is None:
            path.append(node.val)
            result.append(path.copy())
            return
        else:
            target -=node.val
            if node.left:
                self.helper(node.left,target,path+[node.val],result)
            if node.right:
                self.helper(node.right,target,path+[node.val],result)
            target+=node.val
