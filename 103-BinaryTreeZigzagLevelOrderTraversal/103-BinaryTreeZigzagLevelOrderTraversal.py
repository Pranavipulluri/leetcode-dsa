# Last updated: 6/2/2026, 12:03:21 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans=[]
        """if not root:
            return res
        q=collections.deque()
        q.append(root)
        i=0
        while q:
            newlevel=[]
            for _ in range(len(q)):
                node=q.popleft()
                newlevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            i+=1
            res.append(newlevel if i%2!=0 else newlevel[::-1])
        return res"""
        def trvaersal(root,level):
            if not root:
                return
            if len(ans)==level:
                ans.append([])
            if level%2==0:
                ans[level].append(root.val)
            else:
                ans[level].insert(0,root.val)
            trvaersal(root.left,level+1)
            trvaersal(root.right,level+1)
        trvaersal(root,0)
        return ans