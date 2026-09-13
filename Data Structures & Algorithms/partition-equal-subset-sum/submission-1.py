class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False

        target = total // 2

        def dfs(i, currSum, memo):
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            if currSum == target:
                return True

            if currSum > target or i == len(nums):
                return False

            take = dfs(i + 1, currSum + nums[i], memo)
            skip = dfs(i + 1, currSum, memo)
            memo[(i, currSum)] = take or skip
            return memo[(i, currSum)]

        return dfs(0, 0, {})