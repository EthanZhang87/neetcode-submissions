class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, value):
            if value == 0:
                res.append(curr.copy())
                return
            if i == len(candidates) or value < 0:
                return

 

            curr.append(candidates[i])
            dfs(i + 1, curr, value - candidates[i])
            curr.pop()
     

            

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            

            dfs(i + 1, curr, value)

        dfs(0, [], target)

        return res


        



        