# Last updated: 6/2/2026, 12:02:28 PM
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.sortedArr = []
        self.inorderTraverse(root)
        return self.sortedArrayToBST(0, len(self.sortedArr) - 1)

    def inorderTraverse(self, root: TreeNode) -> None:
        if not root:
            return
        self.inorderTraverse(root.left)
        self.sortedArr.append(root)
        self.inorderTraverse(root.right)

    def sortedArrayToBST(self, start: int, end: int) -> TreeNode:
        if start > end:
            return None
        mid = (start + end) // 2
        root = self.sortedArr[mid]
        root.left = self.sortedArrayToBST(start, mid - 1)
        root.right = self.sortedArrayToBST(mid + 1, end)
        return root