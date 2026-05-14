# Last updated: 6/2/2026, 12:03:16 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans=[]
        if not root:
            return []
        q=collections.deque()
        q.append(root)
        while q:
            samelevel=[]
            for _ in range(len(q)):
                node=q.popleft()
                samelevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(samelevel)
        """def traversal(root,level):
            if not root:
                return 
            if len(ans)==level:
                ans.append([])
            if level%2==0:
                ans[level].append(root.val)
            else:
                ans[level].insert(0,root.val)
            traversal(root.left,level+1)
            traversal(root.right,level+1)
        traversal(root,0)"""
        return ans[::-1]