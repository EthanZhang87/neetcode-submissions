# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = True

        def isValidNode(root, min, max):
            nonlocal isValid
            if root.val > min and root.val < max:
                if root.left:
                    isValidNode(root.left, min, root.val)
                if root.right:
                    isValidNode(root.right, root.val, max)
            else:
                isValid = False

            return isValid

        return isValidNode(root, float('-inf'), float('inf'))
            

        