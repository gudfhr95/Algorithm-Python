# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeafNodes(root1) == self.getLeafNodes(root2)

    def getLeafNodes(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        result = []
        if root.left:
            result += self.getLeafNodes(root.left)

        if root.right:
            result += self.getLeafNodes(root.right)

        return result
