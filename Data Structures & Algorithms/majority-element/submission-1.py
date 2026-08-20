class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = count = 0

        for x in nums:
            if count == 0:
                res = x

            count += (1 if x == res else -1)

        return res

        





        