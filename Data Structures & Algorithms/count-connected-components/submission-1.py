class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            while res != par[res]:
                res = par[res]

            return res
        
        def union(u1, u2):
            p1, p2 = find(u1), find(u2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += 1
            else:
                par[p2] = p1
                rank[p1] += 1
            return 1

        res = n
        for x, y in edges:
            res -= union(x, y)

        return res

       

        



        


        