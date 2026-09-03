class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        for x in hand:
            count[x] = count.get(x, 0) + 1

        heap = []

        for k, v in count.items():
            heapq.heappush(heap, k)

        while heap:
            minimum = heap[0]

            for x in range(minimum, minimum + groupSize):
                if x not in count:
                    return False
                count[x] -= 1
                if count[x] == 0 and x != heap[0]:
                    return False
                elif count[x] == 0:
                    heapq.heappop(heap)

        return True

        
        





        return True

        