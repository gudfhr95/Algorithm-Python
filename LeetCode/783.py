class Solution:
    nodes = []

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.nodes = []

        self.dfs(root)

        self.nodes = sorted(self.nodes)

        result = 987654321
        for i in range(1, len(self.nodes)):
            result = min(result, abs(self.nodes[i] - self.nodes[i - 1]))

        return result

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return

        self.nodes.append(root.val)

        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)
