class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(curr, maxVal):
            nonlocal res

            if curr.val >= maxVal:
                res += 1

            maxVal = max(maxVal, curr.val)

            if curr.left:
                dfs(curr.left, maxVal)

            if curr.right:
                dfs(curr.right, maxVal)

        dfs(root, root.val)

        return res