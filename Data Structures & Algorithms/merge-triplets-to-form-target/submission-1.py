class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0]

        for x in triplets:
            if x[0] > target[0] or x[1] > target[1] or x[2] > target[2]:
                continue
                
            res[0] = max(res[0], x[0])
            res[1] = max(res[1], x[1])
            res[2] = max(res[2], x[2])

            if res == target:
                return True

        return False
