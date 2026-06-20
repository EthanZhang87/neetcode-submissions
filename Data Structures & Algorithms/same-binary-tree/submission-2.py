# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 and queue2:
            element1 = queue1.popleft()
            element2 = queue2.popleft()

            if element1 is None and element2 is None:
                continue
    
            if element1 is None or element2 is None or element1.val != element2.val:
                return False
            
            
            queue1.append(element1.left)

           
            queue1.append(element1.right)

            
            queue2.append(element2.left)

            
            queue2.append(element2.right)

        return not queue1 and not queue2