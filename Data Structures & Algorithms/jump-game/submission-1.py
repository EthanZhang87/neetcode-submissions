class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = len(nums) - 1
        for x in range(len(nums) - 2, -1, -1):
            if x + nums[x] >= curr:
                curr = x

        return curr == 0

        