# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = set()

        def dfs(root):
            nonlocal res

            if not root:
                return;

            if root.left:
                res.add(root.left.val)
                dfs(root.left)

            res.add(root.val)

            if root.right:
                res.add(root.right.val)
                dfs(root.right)

        dfs(root)

        return list(res)[k - 1]
        