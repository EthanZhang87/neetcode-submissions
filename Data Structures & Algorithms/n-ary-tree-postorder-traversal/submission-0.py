"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return []
        

        def dfs(curr):
            nonlocal res
            if not curr:
                return

            for x in curr.children:
                dfs(x)

            res.append(curr.val)

        dfs(root)



        return res
        