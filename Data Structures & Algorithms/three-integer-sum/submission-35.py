class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            left = x + 1
            right = len(nums) - 1
            while left < right:
                total = nums[x] + nums[right] + nums[left]

                if total == 0:
                    res.append([nums[x], nums[right], nums[left]])
                    left += 1
                    right -= 1
                
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return res 

