class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        total = 0

        def dfs(i, curr):
            nonlocal total

            if i == len(nums):
                total += curr
                return


            dfs(i + 1, curr ^ nums[i])

            dfs(i + 1, curr)

            return

        dfs(0, 0)

        return total

        