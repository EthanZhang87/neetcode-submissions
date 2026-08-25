class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {x: [] for x in range(n)}
      


        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
       
        visited = set()
        def dfs(curr, parent):
            visited.add(curr)

            for x in adjList[curr]:
                if x == parent:
                    continue

                if x in visited:
                    return False

                if not dfs(x, curr):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n


            
    
        
       


   



       

        
            
        