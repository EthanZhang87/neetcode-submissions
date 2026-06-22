# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        unBalanced = True

        def dfs(root):
            nonlocal unBalanced
            if not root:
                return 0

            right = dfs(root.right)
            left = dfs(root.left)

            if abs(right - left) > 1:
                unBalanced = False
                

            return 1 + max(left, right)

        dfs(root)

        return unBalanced

        
        