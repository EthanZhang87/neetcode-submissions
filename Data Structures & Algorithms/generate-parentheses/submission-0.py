class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def dfs(numOpen, numClose, curr):
            if numClose > numOpen or numOpen > n:
                return

            if numOpen == numClose == n:
                res.append("".join(curr))
                return

            if numOpen < n:
                curr.append('(')
                dfs(numOpen + 1, numClose, curr)
                curr.pop()

            if numClose < numOpen:
                curr.append(')')
                dfs(numOpen, numClose + 1, curr)
                curr.pop()
            
        dfs(0, 0, [])

        return res




        