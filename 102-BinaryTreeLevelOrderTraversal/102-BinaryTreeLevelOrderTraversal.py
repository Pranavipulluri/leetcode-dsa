# Last updated: 6/2/2026, 12:03:23 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res=[]
        if not root:
            return res
        q=collections.deque()
        q.append(root)
        while q:
            newlevel=[]
            for _ in range(len(q)):
                node=q.popleft()
                newlevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(newlevel)
        return res