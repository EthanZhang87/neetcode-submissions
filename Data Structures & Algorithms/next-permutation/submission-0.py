class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        r = len(nums) - 1

        while r > 0 and nums[r] <= nums[r - 1]:
            r -= 1

        if r == 0:
            nums.reverse()
            return

        # Find the smallest element larger than nums[r - 1]
        j = len(nums) - 1

        while nums[j] <= nums[r - 1]:
            j -= 1

        # Swap
        nums[j], nums[r - 1] = nums[r - 1], nums[j]

        # Reverse the remaining portion
        nums[r:] = nums[r:][::-1]