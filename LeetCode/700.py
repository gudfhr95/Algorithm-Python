class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None

        if root.val == val:
            return root

        left = self.searchBST(root.left, val)
        right = self.searchBST(root.right, val)

        if left != None:
            return left

        if right != None:
            return right

        return None
