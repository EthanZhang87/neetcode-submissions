class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for x in range(len(nums) - 1, -1, -1):
            for j in range(x + 1, len(nums)):
                if nums[x] < nums[j]:
                    LIS[x] = max(LIS[x], 1 + LIS[j])

        return max(LIS)



        