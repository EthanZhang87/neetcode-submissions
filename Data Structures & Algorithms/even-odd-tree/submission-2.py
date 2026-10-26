# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0

        queue = deque([root])

        while queue:
            prev = None
            for x in range(len(queue)):
                ele = queue.popleft()
                if level % 2 == 0:
                    if ele.val % 2 == 0 or (prev is not None and ele.val <= prev):
                        return False
                else:
                    if ele.val % 2 == 1 or (prev is not None and ele.val >= prev):
                        return False

                prev = ele.val

                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)

            level += 1
        return True

        