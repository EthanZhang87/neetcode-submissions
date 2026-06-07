class Solution:
    def climbStairs(self, n: int) -> int:
        

        def dfs(integer):

            if integer >= n:
                return integer == n
            return dfs(integer + 1) + dfs(integer + 2)

        return dfs(0)





        