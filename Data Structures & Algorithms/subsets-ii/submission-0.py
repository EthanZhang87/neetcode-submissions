class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        visited = set()

        def dfs(i, curr):

            if i >= len(nums):
                if tuple(curr) in visited:
                    return
                visited.add(tuple(curr))
                res.append(curr.copy())
                return


            curr.append(nums[i])
            dfs(i + 1, curr)

            curr.pop()

            dfs(i + 1, curr)

        dfs(0, [])

        return res


            
        