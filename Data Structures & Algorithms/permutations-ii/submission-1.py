class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for x in count:
                if count[x] > 0:
                    curr.append(x)
                    count[x] -= 1
                    dfs(curr)

                    curr.pop()
                    count[x] += 1

            return

        dfs([])

        return res

        