class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outGoing = defaultdict(int)
        inComing = defaultdict(int)

        for x in trust:
            outGoing[x[0]] += 1
            inComing[x[1]] += 1

        for x in range(1, n + 1):
            if outGoing[x] == 0 and inComing[x] == n - 1:
                return x

        return -1
        