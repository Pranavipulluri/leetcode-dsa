# Last updated: 6/2/2026, 12:03:05 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        self.flatten(root.left)
        self.flatten(root.right)
        temp=root.right
        root.right=root.left
        root.left=None
        curr=root
        while curr.right:
            curr=curr.right
        curr.right=temp