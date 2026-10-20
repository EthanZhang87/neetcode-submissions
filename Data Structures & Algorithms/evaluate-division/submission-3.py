class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for x in range(len(equations)):
            adj[equations[x][0]].append([equations[x][1], values[x]])
            adj[equations[x][1]].append([equations[x][0], 1 / values[x]])


        res = []


        def dfs(src, target, visited):
            if src not in adj or target not in adj:
                return -1

            if src == target:
                return 1

            visited.add(src)

            for nei, weight in adj[src]:
                if nei not in visited:
                    result = dfs(nei, target, visited)
                    if result != -1:
                        return weight * result

            return -1

        return [dfs(q[0], q[1], set()) for q in queries]
