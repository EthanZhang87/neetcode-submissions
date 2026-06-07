class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for x in nums:
            dic[x] = 1 + dic.get(x,0)

        arr = [[] for x in range(len(nums) + 1)]

        for e,v in dic.items():
            arr[v].append(e)

        res = []
        for x in range(len(arr) - 1, 0, -1):
            for y in arr[x]:
                res.append(y)
                if len(res) == k:
                    return res




        