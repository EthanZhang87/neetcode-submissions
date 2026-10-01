class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        res = 1
        prev = 0
  

        for r in range(1, len(arr)):
            if arr[r] > arr[r - 1]:
                curr = 1
            elif arr[r] < arr[r - 1]:
                curr = -1
            else:
                curr = 0

            if curr == 0:
                l = r

            elif curr == prev:
                l = r - 1

            res = max(res, r - l + 1)

            prev = curr

        return res

            


        