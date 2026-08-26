# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        
        def dfs(curr1, curr2):
            if curr1.val != curr2.val:
                return False

            if (not curr1 and curr2) or (not curr2 and curr1):
                return False
            

            if curr1.left or curr2.left:
                if not curr1.left or not curr2.left:
                    return False

                if curr1.left.val == curr2.left.val:
                    if not dfs(curr1.left, curr2.left):
                        return False
                else:
                    return False

            if curr1.right or curr2.right:
                if not curr1.right or not curr2.right:
                    return False
                if curr1.right.val == curr2.right.val:
                    if not dfs(curr1.right, curr2.right):
                        return False
                else:
                    return False

            return True

        return dfs(p, q)

        
        