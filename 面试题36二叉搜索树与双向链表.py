"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return 
        result = []
        self.helper(root,result)
        head = Node(result[0],None,None)
        cur = head
        for i in range(1,len(result)):
           node = Node(result[i],None,None)
           cur.right = node
           node.left = cur
           cur = cur.right
        
        head.left = cur
        cur.right = head
        return head  

    def helper(self,root,result):
        if root:
            self.helper(root.left,result)
            result.append(root.val)
            self.helper(root.right,result)
        return result