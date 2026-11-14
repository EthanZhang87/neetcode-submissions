class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = []
        for x in nums:
            if x not in visited:
                visited.append(x)

            else:
                return True

        return False
        