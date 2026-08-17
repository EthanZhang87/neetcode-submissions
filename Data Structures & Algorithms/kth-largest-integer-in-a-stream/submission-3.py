class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        heap = []
        self.nums.append(val)
        for x in self.nums:
            heapq.heappush(heap, x)

        while heap:
            if len(heap) == self.k:
                return heapq.heappop(heap)
            heapq.heappop(heap)

        
