class NumArray:

    def __init__(self, nums: List[int]):
        self.sumMat = [0] * len(nums)
        prefix = 0
        for x in range(len(nums)):
            prefix += nums[x]
            self.sumMat[x] = prefix

        

        
        

    def sumRange(self, left: int, right: int) -> int:
        if left <= 0:
            return self.sumMat[right]
        return self.sumMat[right] - self.sumMat[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)