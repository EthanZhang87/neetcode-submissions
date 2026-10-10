class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)


        def find(node):
            while node != par[node]:
                node = par[node]

            return node


        def union(u1, u2):
            p1, p2 = find(u1), find(u2)

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p1] += 1
            else:
                par[p2] = p1
                rank[p2] += 1

        for x,y in edges:
            if find(x) == find(y):
                return [x, y]
            else:
                union(x, y)

            