# Last updated: 6/2/2026, 12:03:13 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow=head
        fast=head
        solw_prev=None
        while fast and fast.next:
            slow_prev=slow
            slow=slow.next
            fast=fast.next.next
        slow_prev.next=None
        node=TreeNode(slow.val)
        node.left=self.sortedListToBST(head)
        node.right=self.sortedListToBST(slow.next)
        return node