# Last updated: 6/2/2026, 12:03:42 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        temp = dummy
        curr = head

        while curr:
            # case: duplicate sequence begins
            if curr.next and curr.val == curr.next.val:
                dup = curr.val
                # skip all nodes with value dup
                while curr and curr.val == dup:
                    curr = curr.next
            else:
                # unique value → attach to result
                temp.next = curr
                temp = temp.next
                curr = curr.next

        temp.next = None   # IMPORTANT: cut off old links
        return dummy.next
