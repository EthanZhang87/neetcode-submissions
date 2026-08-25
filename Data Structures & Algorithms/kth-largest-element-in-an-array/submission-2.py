class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for x in nums:
            heapq.heappush(heap,  x)

        while heap:
            if len(heap) == k:
                return heapq.heappop(heap)
            heapq.heappop(heap)

        