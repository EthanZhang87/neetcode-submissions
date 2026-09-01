class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] >= target:
                return 1
            else:
                return 0
        res = float('inf')

        l = 0

        curr = 0

        for r in range(len(nums)):
            curr += nums[r]

            while curr >= target:
                if res > r - l + 1:
                    res = r - l + 1
                curr -= nums[l]
                l += 1

        if curr < target and l == 0:
            return 0

        return res

        