# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if not pNode.left and not pNode.right and not pNode.next:
            return None
        if pNode.right:
            result = pNode.right
            while result.left:
                result = result.left
            return result
        
        while pNode.next:
            father = pNode.next
            if father.left== pNode:
                return father
            pNode = father
        return None