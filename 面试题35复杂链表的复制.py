"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        d = {}
        pointer = head
        newHead = Node(0,None,None)
        cur = newHead
        d[head] = newHead
        while pointer:
            newNode = Node(pointer.val,None,None)
            d[pointer] = newNode
            cur.next = newNode
            cur = cur.next
            pointer = pointer.next
        pointer = head
        while pointer:
            if pointer.random:
                d[pointer].random = d[pointer.random]
            pointer = pointer.next
        return newHead.next
        
        
