class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())

                return

            for x in range(len(nums)):
                if nums[x] in visited:
                    continue

                visited.add(nums[x])
                curr.append(nums[x])

                dfs(curr)

                curr.pop()
                visited.remove(nums[x])

        dfs([])

        return res
        