class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = {i: [] for i in range(len(points))}

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append([distance, j])
                adjList[j].append([distance, i])

        heap = [[0, 0]]
        res = 0
        visited = set()

        while len(visited) < len(points):
            ele = heapq.heappop(heap)
            if ele[1] in visited:
                continue
            res += ele[0]
            visited.add(ele[1])
            for nei in adjList[ele[1]]:
                if nei[1] not in visited:
                    heapq.heappush(heap, [nei[0], nei[1]])

        return res


        
