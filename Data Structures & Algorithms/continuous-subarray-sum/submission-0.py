class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        cache = {0: -1}

        curr = 0

        for x in range(len(nums)):
            curr += nums[x]

            if curr % k in cache:
                if x - cache[curr % k] > 1:
                    return True

            else:
                cache[curr % k] = x

        return False

            



        