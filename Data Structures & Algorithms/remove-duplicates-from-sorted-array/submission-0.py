class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        r = 1

        while r < len(nums):
            while r < len(nums) and nums[r] == nums[r - 1]:
                r += 1

            if r < len(nums):
                nums[l] = nums[r]

                l += 1
                r += 1

        return l


        