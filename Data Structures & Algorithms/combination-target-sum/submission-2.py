class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, value):

            if value < 0:
                return 

            if value == 0:
                res.append(curr.copy())

                return

            for x in range(i, len(nums)):
                curr.append(nums[x])
                dfs(x, curr, value - nums[x])
                curr.pop()
                

            return

        dfs(0, [], target)

        return res

        
            
        
