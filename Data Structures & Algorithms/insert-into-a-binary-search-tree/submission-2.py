# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return TreeNode(val)

        insertionRoot = None
        def dfs(root):
            nonlocal insertionRoot
            if not root:
                return

            if root.val < val:
                insertionRoot = root
                dfs(root.right)

            if root.val > val:
                insertionRoot = root
                dfs(root.left)


            return

        dfs(root)

        if insertionRoot.val < val:
            insertionRoot.right = TreeNode(val)
        else:
            insertionRoot.left = TreeNode(val)

        return root



        