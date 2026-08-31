class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        everyTrust = [True] * (n + 1)
        adjList = {i: [] for i in range(1, n + 1)}

        for x in trust:
            adjList[x[0]].append(x[1])


        curr = None
        for x, y in adjList.items():
            if not adjList[x]:
                curr = x
            for i in range(1, n + 1):
                if i != curr and i not in adjList[x]:
                    everyTrust[i] = False

        if curr is not None and everyTrust[curr]:
            return curr

        return -1
        