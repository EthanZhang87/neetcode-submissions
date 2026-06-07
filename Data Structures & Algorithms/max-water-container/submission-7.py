class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        left, right = 0, len(heights) - 1

        while left < right:
            volume = min(heights[left], heights[right]) * (right - left)

            if volume > max:
                max = volume

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max