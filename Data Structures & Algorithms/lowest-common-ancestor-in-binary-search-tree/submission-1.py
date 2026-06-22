# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == p or root == q:
            return root

        queue = deque([root])

        while queue:
            element = queue.popleft()
            if (element.val >= p.val and element.val <= q.val) or (element.val <= p.val and element.val >= q.val):
                return element

            queue.append(element.left)
            queue.append(element.right)

        
                
        