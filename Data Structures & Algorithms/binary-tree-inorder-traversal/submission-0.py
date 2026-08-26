# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []

        def dfs(curr):
            if not curr.left and not curr.right:
                res.append(curr.val)
                return

            if curr.left:
                dfs(curr.left)

            res.append(curr.val)

            if curr.right:
                dfs(curr.right)

        dfs(root)

        return res
                
        