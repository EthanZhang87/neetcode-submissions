class UnionFind:
    def __init__(self, n):
        self.pars = [x for x in range(n)]
        self.rank = [1] * n

    def find(self, curr):
        while curr != self.pars[curr]:
            curr = self.pars[curr]

        return curr

    def union(self, u1, u2):
        p1, p2 = self.find(u1), self.find(u2)
        if p1 == p2:
            return

        if self.rank[p1] > self.rank[p2]:
            self.pars[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.pars[p1] = p2
            self.rank[p2] += self.rank[p1]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        emailGroup = defaultdict(list)

        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)

        res = []

        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))

        return res

        