# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        # count = 0
        # cur = head
        # while cur:
        #     cur = cur.next
        #     count+=1
        # count -=k
        # cur = head
        # while cur:
        #     if count == 0:
        #         return cur
        #     count-=1
        #     cur = cur.next
        # if count>0:
        #     return None
        former,latter = head,head
        for _ in range(k):
            if former is None:
                return None
            former = former.next
        while former:
            latter = latter.next
            former = former.next
        return latter

