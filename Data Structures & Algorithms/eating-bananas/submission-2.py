class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2

            res = 0
            for x in piles:
                res += math.ceil(float(x) / mid)

            if res <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


        