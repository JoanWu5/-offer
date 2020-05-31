# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # if len(preorder) == 0 or len(inorder) ==0:
        #     return None
        # node = TreeNode(preorder[0])
        # index = inorder.index(preorder[0])
        # node.left = self.buildTree(preorder[1:index+1],inorder[:index])
        # node.right = self.buildTree(preorder[index+1:],inorder[index+1:])
        # return node

        #优化index
        if len(preorder) == 0 or len(inorder) ==0:
            return None
        self.d = {}
        self.po = preorder
        for i in range(len(inorder)):
            self.d[inorder[i]] = i
        return self.helper(0,0,len(preorder)-1)
    
    def helper(self, pre_root,start,end):
        if start>end:
            return None
        node = TreeNode(self.po[pre_root])
        index = self.d[self.po[pre_root]]
        node.left = self.helper(pre_root+1,start,index-1)
        node.right = self.helper(index-start+pre_root+1,index+1,end)
        return node
        
        