class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        currMin, currMax = 1, 1

        for x in nums:
            
            temp = currMin * x
            currMin = min(currMin * x, currMax * x, x)
            currMax = max(currMax * x,  temp, x)

            res = max(res, currMax)

        return res
        
            
           

            


        


            
        