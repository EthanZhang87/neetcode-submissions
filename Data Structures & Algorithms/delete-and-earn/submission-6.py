class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        arr = sorted(set(nums))
        memo = {}

        def dfs(i):
            if i >= len(arr):
                return 0

            if i in memo:
                return memo[i]

            # Option 1: Skip current number
            skip = dfs(i + 1)

            # Option 2: Take current number
            currEarn = arr[i] * count[arr[i]]

            if i + 1 < len(arr) and arr[i + 1] == arr[i] + 1:
                take = currEarn + dfs(i + 2)
            else:
                take = currEarn + dfs(i + 1)

            memo[i] = max(take, skip)
            return memo[i]

        return dfs(0)