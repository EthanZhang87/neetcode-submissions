class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        res = [0] * len(heights)
        stack = []


        for i in range(len(heights)):
            while stack and stack[-1][0] < heights[i]:
                ele = stack.pop()
                res[ele[1]] += 1

            if stack:
                res[stack[-1][1]] += 1

            stack.append([heights[i], i])

        return res

        