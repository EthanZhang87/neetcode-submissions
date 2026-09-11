class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k
        res = [0] * k

        def dfs(i):
            if i == len(nums):
                return True

            for j in range(k):
                if res[j] + nums[i] <= target:
                    res[j] += nums[i]

                    if dfs(i + 1):
                        return True

                    res[j] -= nums[i]

                    if res[j] == 0:   # <-- this line is the key fix
                        break

            return False

        return dfs(0)