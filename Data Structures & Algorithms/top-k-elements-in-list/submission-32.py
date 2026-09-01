class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        res = []
        count = Counter(nums)

        for i, v in count.items():
            heapq.heappush(heap, (-1 * v, i))

        length = len(heap)

        while heap:
            res.append(heapq.heappop(heap)[1])
            if len(res) == k:
                return res

    

     



        





        