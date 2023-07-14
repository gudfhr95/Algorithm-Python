class Solution:
    result = []

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.result = []
        self.dfs(root)

        node = TreeNode(self.result[0])
        cur = node
        for i in range(1, len(self.result)):
            cur.right = TreeNode(self.result[i])
            cur = cur.right

        return node

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return

        self.dfs(root.left)
        self.result.append(root.val)
        self.dfs(root.right)
