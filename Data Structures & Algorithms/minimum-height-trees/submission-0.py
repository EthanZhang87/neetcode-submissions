class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for start, end in edges:
            adjList[start].append(end)
            adjList[end].append(start)

        heights = {i: 1 for i in range(n)}


        def dfs(curr, visited):
            visited.add(curr)
            height = 0
            for nei in adjList[curr]:
                if nei not in visited:
                    height = max(height, 1 + dfs(nei, visited))


            return height

        for i in range(n):
            heights[i] = dfs(i, set())

        minHeight = min(heights.values())

        return [x for x in heights if heights[x] == minHeight]



        




