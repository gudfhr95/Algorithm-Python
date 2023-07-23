class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        result = 0
        if low <= root.val and root.val <= high:
            result += root.val

        result += self.rangeSumBST(root.left, low, high)
        result += self.rangeSumBST(root.right, low, high)

        return result
