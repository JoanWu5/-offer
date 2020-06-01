# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        # pre = head
        # cur = head.next
        # while cur:
        #     if pre.val != cur.val:
        #         pre.next = cur
        #         pre = cur
        #     cur = cur.next
        # pre.next = None
        # return head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head



            
