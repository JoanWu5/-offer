# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if head is None:
            return []
        #时间O(n) 空间O(n)
        # result = []
        # while head!= None:
        #     result.insert(0,head.val)
        #     head = head.next
        # return result

        # result = []
        # while head!=None:
        #     result.append(head.val)
        #     head = head.next
        # return result[::-1]

        return self.reversePrint(head.next)+[head.val]
        