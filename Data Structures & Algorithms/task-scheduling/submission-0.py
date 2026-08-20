class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-count for count in count.values()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0


        while maxHeap or queue:
            time += 1
            if maxHeap:
                element = heapq.heappop(maxHeap)
                element += 1

                if element < 0:
                    queue.append((element, time + n))

            if queue:
                if queue[0][1] == time:
                    heapq.heappush(maxHeap, queue[0][0])
                    queue.popleft()


        return time




                