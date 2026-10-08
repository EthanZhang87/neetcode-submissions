# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(root, canTake, memo):

            if not root:
                return 0

            if (root, canTake) in memo:
                return memo[(root, canTake)]
            
                
            dontTakeRight = dfs(root.right, True, memo)
            dontTakeLeft = dfs(root.left, True, memo)
            takeRight = root.val + dfs(root.right, False, memo)
            takeLeft = root.val + dfs(root.left, False, memo)

            dontTake = dontTakeRight + dontTakeLeft
            take = takeRight + takeLeft - root.val
            

            if canTake:
                memo[(root, canTake)] = max(dontTake, take)
                return memo[(root, canTake)]
            memo[(root, canTake)] = dontTake
            return memo[(root, canTake)]

        return dfs(root, True, {})

            
            