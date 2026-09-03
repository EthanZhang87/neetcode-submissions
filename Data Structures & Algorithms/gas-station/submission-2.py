class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        res = 0
        curr = 0

        for x in range(len(gas)):
            curr += gas[x] - cost[x]

            if curr < 0:
                res = x + 1
                curr = 0

        return res