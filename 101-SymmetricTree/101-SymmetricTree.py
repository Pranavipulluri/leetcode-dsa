# Last updated: 6/2/2026, 12:03:24 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def ismirror(n1,n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            return n1.val==n2.val and ismirror(n1.left,n2.right) and ismirror(n1.right,n2.left)
        return ismirror(root.left,root.right)