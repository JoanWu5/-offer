# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while cur and cur.next:
            if pre.next.val != cur.next.val:
                pre = pre.next
                cur = cur.next
            else:
                while cur and cur.next and pre.next.val==cur.next.val:
                    cur = cur.next
                pre.next = cur.next
                cur = cur.next
        return dummy.next

s = Solution()
root = ListNode(1)
root.next = ListNode(1)
print(s.deleteDuplicates(root))