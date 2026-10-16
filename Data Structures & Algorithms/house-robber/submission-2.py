class Solution:
    def rob(self, nums: List[int]) -> int:


        def dfs(i, memo):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0

            skip = dfs(i + 1, memo)
            rob = nums[i] + dfs(i + 2, memo)

            memo[i] = max(skip, rob)
            return memo[i]

        return dfs(0, {})
        