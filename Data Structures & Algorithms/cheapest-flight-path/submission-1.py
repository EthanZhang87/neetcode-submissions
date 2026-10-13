class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)

        for f, t, weight in flights:
            adjList[f].append([t, weight])


    
        res = {}
        heap = [[0, src, 0]]

        while heap:

            
            ele = heapq.heappop(heap)


            if (ele[1], ele[2]) in res:
                continue

            res[(ele[1], ele[2])] = ele[0]



            if ele[1] == dst:
                return ele[0]

            if ele[2] == k + 1:
                continue

            for nei in adjList[ele[1]]:
                heapq.heappush(heap, [ele[0] + nei[1], nei[0], ele[2] + 1])

        return -1

            


