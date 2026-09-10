class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        heap = []
        passengers = 0

        for x in trips:

            while heap and heap[0][0] <= x[1]:
                end, people = heapq.heappop(heap)
                passengers -= people

            passengers += x[0]

            if passengers > capacity:
                return False

            heapq.heappush(heap, (x[2], x[0]))

        return True

            



