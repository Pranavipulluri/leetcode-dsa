# Last updated: 6/2/2026, 12:03:18 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        preorder=deque(preorder)
        def build(preorder,inorder):
            if inorder:
                idx=inorder.index(preorder.popleft())
                root=TreeNode(inorder[idx])
                root.left=build(preorder,inorder[:idx])
                root.right=build(preorder,inorder[idx+1:])
                return root
        return build(preorder,inorder)