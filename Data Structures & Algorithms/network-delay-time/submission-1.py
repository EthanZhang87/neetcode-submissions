class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = 0

        adjList = defaultdict(list)

        for src, dst, weight in times:
            adjList[src].append((dst, weight))

        shortest = {}
        heap = [[0, k]]

        while heap:
            ele = heapq.heappop(heap)
            if ele[1] not in shortest:
                shortest[ele[1]] = ele[0]

                for nei, weight in adjList[ele[1]]:
                    if nei not in shortest:
                        heapq.heappush(heap, [ele[0] + weight, nei])
        
        for x in range(1, n + 1):
            if x not in shortest:
                return -1

        res = 0

        for key, val in shortest.items():
            res = max(res, val)

        return res