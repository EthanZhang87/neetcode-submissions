class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

        

    def addNum(self, num: int) -> None:
        if len(self.minHeap) + len(self.maxHeap) == 0:
            heapq.heappush(self.minHeap, num)
          

        else:

            if len(self.minHeap) > len(self.maxHeap):
                if self.minHeap[0] < num:
                    heapq.heappush(self.maxHeap, -1 * (heapq.heappop(self.minHeap)))
                    heapq.heappush(self.minHeap, num)

                else:
                    heapq.heappush(self.maxHeap, -1 * num)

            else:
                if -1 * self.maxHeap[0] > num:
                    heapq.heappush(self.minHeap, -1 * (heapq.heappop(self.maxHeap)))
                    heapq.heappush(self.maxHeap, -1 * num)
                else:
                    heapq.heappush(self.minHeap, num)

        

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]

        else:
            return (self.minHeap[0] + -1 * self.maxHeap[0]) / 2
        
        