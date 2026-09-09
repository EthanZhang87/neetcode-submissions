class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)


        stack = []

        for x in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[x]:
                res[stack[-1][1]] = x - stack[-1][1]
                stack.pop()

            stack.append((temperatures[x], x))

        return res
