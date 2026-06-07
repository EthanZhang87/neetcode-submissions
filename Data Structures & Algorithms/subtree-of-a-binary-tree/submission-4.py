# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        visited = set()
        stack = [root]

        while stack:
            popped = stack.pop()
            if popped not in visited:
                visited.add(popped)

            if popped.val == subRoot.val and self.sameTree(popped, subRoot):
                return True
            if popped.left:
                stack.append(popped.left)
            if popped.right:
                stack.append(popped.right)
        return False
        

    

    def sameTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False

        return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)