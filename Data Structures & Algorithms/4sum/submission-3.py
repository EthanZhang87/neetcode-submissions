class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for x in range(i + 1, len(nums)):
                if x > i + 1 and nums[x] == nums[x - 1]:
                    continue

                l, r = x + 1, len(nums) - 1

                while l < r:
                    if nums[r] + nums[x] + nums[l] + nums[i] == target:
                        res.append([nums[i], nums[x], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1    

                        while r > l and nums[r] == nums[r + 1]:
                            r -= 1

                    elif nums[r] + nums[x] + nums[l] + nums[i] > target:
                        r -= 1
                    else:
                        l += 1

        return res

                        