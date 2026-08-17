class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for x in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[x]:
                val, pos = stack.pop()
                res[pos] = x - pos

            stack.append((temperatures[x], x))

        return res

        