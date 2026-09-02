class Solution:
    def check(self, nums: List[int]) -> bool:
        wrong = 0

        for x in range(len(nums)):
            if nums[x] < nums[(x-1)]:
                wrong += 1

        if wrong <= 1:
            return True

        return False

        