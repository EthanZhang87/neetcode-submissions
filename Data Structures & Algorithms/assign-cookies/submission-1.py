class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        heap1 = []
        heap2 = []

        for x in g:
            heapq.heappush(heap1, x)

        for x in s:
            heapq.heappush(heap2, x)

        res = 0
        while heap1 and heap2:
            child = heap1[0]
            cookie = heapq.heappop(heap2)

            if cookie >= child:
                heapq.heappop(heap1)
                res += 1

        return res