class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        

        for x in points:
            distance = math.sqrt((x[0]**2) + (x[1]**2))
            heapq.heappush(heap, (distance, x))

        removed = 0

        while removed < k:
            res.append(heapq.heappop(heap)[1])
            removed += 1

        return res
            