class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]


        def dfs(i, end, memo):
            if (i, end) in memo:
                return memo[(i, end)]
            if i > end:
                return 0


            rob = nums[i] + dfs(i + 2, end, memo)
            skip = dfs(i + 1, end, memo)
            memo[(i, end)] = max(rob, skip)
            return memo[(i, end)]

        return max(dfs(0, len(nums) - 2, {}), dfs(1, len(nums) - 1, {}))
        