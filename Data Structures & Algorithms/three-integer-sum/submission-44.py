class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for x in range(len(nums)):
            if x>0 and nums[x] == nums[x - 1]:
                continue
            
            l, r = x + 1, len(nums) - 1

            while l < r:
                if nums[x] + nums[l] + nums[r] == 0:
                    res.append([nums[x], nums[l] ,nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1  
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1    
                elif nums[x] + nums[l] + nums[r] < 0:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    r -= 1
   

        return res
            
                

