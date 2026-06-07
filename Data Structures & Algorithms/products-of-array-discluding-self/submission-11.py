class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        multiply = 1

        for x in nums:
                multiply *= x

        arr = []

        for i in range(len(nums)):
            if nums[i] != 0:
                arr.append(int(multiply/nums[i]))
            else:
                newProduct = 1
                for x in range(len(nums)):
                    if x != i:
                        newProduct *= nums[x]

                arr.append(newProduct)

        return arr
