class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cur = 0
        pre = {0:1}


        for n in nums:
            cur += n

            diff = cur - k

            res += pre.get(diff, 0)

            pre[cur] = pre.get(cur, 0) + 1
        return res
        


        