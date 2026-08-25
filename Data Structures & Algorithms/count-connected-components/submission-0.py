class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}

        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
        res = 0
     
        visit = [False] * n


        def dfs(curr):
            for x in adjList[curr]:
                if not visit[x]:
                    visit[x] = True

                    dfs(x)

        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1

        return res

       

        



        


        