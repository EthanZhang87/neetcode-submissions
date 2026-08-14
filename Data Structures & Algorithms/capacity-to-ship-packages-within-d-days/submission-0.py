class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            ships = 1
            currCap = cap
            for x in weights:
                if currCap - x < 0:
                    ships += 1
                    currCap = cap
                currCap -= x

            return ships <= days

        while l <= r:
            mid = (l + r) // 2

            if canShip(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res
           


        