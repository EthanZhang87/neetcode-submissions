class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(i, sum, memo):
            if (i, sum) in memo:
                return memo[(i, sum)]
            if i == len(nums):
                if sum == target:
                    return 1
                else:
                    return 0

            

            memo[(i, sum)] = dfs(i + 1, sum - nums[i], memo) + dfs(i + 1, sum + nums[i], memo)

            return memo[(i, sum)]

        return dfs(0, 0, {})
            

        