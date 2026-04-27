# Last updated: 6/2/2026, 12:02:53 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0)  # Dummy node
        dummy.next = head
        current = dummy  # Pointer to traverse
        
        while current.next:
            if current.next.val == val:
                current.next = current.next.next  # Remove node
            else:
                current = current.next  # Move forward
        
        return dummy.next  # Return new head

        