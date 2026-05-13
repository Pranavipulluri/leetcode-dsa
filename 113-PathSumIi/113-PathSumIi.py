# Last updated: 6/2/2026, 12:03:07 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        ans=[]
        def pathhh(root,targetSum,path):
            if not root:
                return False
            else:
                path.append(root.val)
            if not root.left and not root.right:
                if targetSum==root.val:
                    ans.append(path[:])
            pathhh(root.left,targetSum-root.val,path)
            pathhh(root.right,targetSum-root.val,path)
            path.pop()
        pathhh(root,targetSum,[])
        return ans