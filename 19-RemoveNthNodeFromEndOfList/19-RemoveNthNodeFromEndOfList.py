# Last updated: 6/2/2026, 12:05:15 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        length = 0
        temp = head
        
        while temp:
            length += 1
            temp = temp.next
        
        temp = dummy
        for _ in range(length - n):
            temp = temp.next
        
        temp.next = temp.next.next
        
        return dummy.next
