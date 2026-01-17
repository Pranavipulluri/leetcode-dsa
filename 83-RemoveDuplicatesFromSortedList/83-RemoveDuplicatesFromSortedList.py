# Last updated: 6/2/2026, 12:03:40 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        
        cn = head.val
        temp = head
        
        while temp.next is not None:
            if temp.next.val == cn:
                temp.next = temp.next.next   # delete duplicate
            else:
                cn = temp.next.val          # update new current number
                temp = temp.next            # move forward
        
        return head
