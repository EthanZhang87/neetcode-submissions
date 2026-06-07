class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        includesZero = 0
        for x in nums:
            if x == 0:
                includesZero += 1
            else:
                total = total * x

        for x in range(len(nums)):
            if nums[x] == 0 and includesZero == 1:
                nums[x] = total 
            elif includesZero >= 1:
                nums[x] = 0
            else:
                nums[x] = int(total/nums[x])

        return nums        