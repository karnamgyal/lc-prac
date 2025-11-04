# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None

        p1, p2 = head, head
        prev1 = None
        while (p2 != None and p2.next != None):
            prev1 = p1
            p1 = p1.next
            p2 = p2.next.next
        prev1.next = p1.next
        return head