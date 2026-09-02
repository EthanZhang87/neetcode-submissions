class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for r in range(len(nums) - 2, -1, -1):
            if r + nums[r] >= goal:
                goal = r

        return goal == 0
        