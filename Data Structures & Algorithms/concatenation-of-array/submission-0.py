class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums[:]
        for x in nums:
            ans.append(x)

        return ans
        