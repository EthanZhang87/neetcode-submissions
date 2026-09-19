class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        res = 0

        def dfs(i, curr, memo):
            if (i, curr) in memo:
                return memo[(i, curr)]
            count = 0

            if curr == amount:
                return 1

            if i == len(coins) or curr > amount:
                return 0

            count += dfs(i, curr + coins[i], memo)
            count += dfs(i + 1, curr, memo)

            memo[(i, curr)] = count

            return memo[(i, curr)]

        return dfs(0, 0, {})

            
        