class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

      
        lastMoveLeft = False
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                r = mid - 1
                lastMoveLeft = True
               

            else:
                l = mid + 1
   
                lastMoveLeft = False

        if lastMoveLeft:
            return mid
        return mid + 1
        