class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newArr = []
        for x in nums:
            if x not in newArr:
                newArr.append(x)
            else:
                return True

        return False