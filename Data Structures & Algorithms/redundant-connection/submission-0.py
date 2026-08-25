class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(1, len(edges) + 1)}
        queue = deque()
        inDegree = [0] * (len(edges) + 1)
        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
            inDegree[x] += 1
            inDegree[y] += 1

        for x in adjList:
            if inDegree[x] == 1:
                queue.append(x)

        while queue:
            element = queue.popleft()
            inDegree[element] -= 1
            for x in adjList[element]:
                inDegree[x] -= 1
                if inDegree[x] == 1:
                    queue.append(x)





        


        
        for u, v in reversed(edges):
            if inDegree[u] == 2 and inDegree[v]:
                return [u, v]

        return []

        