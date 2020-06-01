# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        #时间复杂度O(n)
        if head is None:
            return None
        if head.val == val:
            return head.next
        cur = head 
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head

        #当val是ListNode型时，就是说是head的某一部分，需要删除val开始的节点,时间复杂度O(1)
        if head is None or val is None:
            return head
        if val.next is not None:
            temp = val.next
            val.val = temp.val
            val.next = temp.next
        elif head == val:
            head = None
        else:
            cur = head
            while cur.next!=val:
                cur = cur.next
            cur.next = None
        return head

        