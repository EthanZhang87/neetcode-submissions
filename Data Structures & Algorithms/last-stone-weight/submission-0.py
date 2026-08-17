class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for x in stones:
            heapq.heappush(heap, -1 * x)

        

        while len(heap) > 1:
            ele1 = -1 * heapq.heappop(heap)
            ele2 = -1 * heapq.heappop(heap)

            if ele1 == ele2:
                continue

            if ele1 > ele2:
                heapq.heappush(heap, -1 * (ele1 - ele2))

 
        try:
            return -1 * heapq.heappop(heap)

        except:
            return 0
        