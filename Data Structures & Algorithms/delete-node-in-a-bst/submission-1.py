# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root.val == key:
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            temp = root.right

            leftmost = temp
            while leftmost.left:
                leftmost = leftmost.left

            leftmost.left = root.left

            return temp

        prevNode = None

        def dfs(root):
            nonlocal prevNode
            if not root:
                return

            if root.val == key:
                if prevNode is None:
                    return
                if root.val < prevNode.val:
                    if root.left and root.right:
                        temp = root.right
                        prevNode.left = temp
                        temp.left = root.left

                    else:
                        prevNode.left = root.left or root.right

                else:
                    if root.left and root.right:
                        temp = root.right
                        prevNode.right = temp
                        temp.left = root.left

                    else:
                        prevNode.right = root.left or root.right

                return

            if root.val < key:
                prevNode = root
                dfs(root.right)

            if root.val > key:
                prevNode = root
                dfs(root.left)


        dfs(root)

        return root

        