class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, value):

            if value < 0:
                return 

            if value == 0:
                res.append(curr.copy())

                return

            if i == len(nums):
                return

            curr.append(nums[i])

            dfs(i, curr, value - nums[i])
            curr.pop()
            dfs(i + 1, curr, value)
                

            return

        dfs(0, [], target)

        return res

        
            
        
