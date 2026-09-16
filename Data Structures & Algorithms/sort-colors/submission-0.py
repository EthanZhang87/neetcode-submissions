class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3

        for x in nums:
            count[x] += 1

        counter = 0
        for x in range(len(nums)):
            if count[counter] > 0:
                nums[x] = counter
                count[counter] -= 1

            else:
                while count[counter] <= 0:
                    counter += 1

                nums[x] = counter
                count[counter] -= 1

                        
        