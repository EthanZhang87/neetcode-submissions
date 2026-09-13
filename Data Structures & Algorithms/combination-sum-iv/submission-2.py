class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        def dfs(currSum, memo):
            count = 0
            if currSum in memo:
                return memo[currSum]
            if currSum == target:
                return 1

            if currSum > target:
                return 0

            for num in nums:
                count += dfs(currSum + num, memo)
            memo[currSum] = count
            return count

        return dfs(0, {})

       