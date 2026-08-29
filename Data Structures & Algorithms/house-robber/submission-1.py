class Solution:
    def rob(self, nums: List[int]) -> int:
        
        res = 0

        def dfs(i, memo):

            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            rob = nums[i] + dfs(i + 2, memo)
            skip = dfs(i + 1, memo)


            

            memo[i] = max(rob, skip)
            return memo[i]

        return dfs(0, {})





            

        


            

        
             
        