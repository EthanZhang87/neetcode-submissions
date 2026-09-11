class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = 0
        l, r = 0, len(arr) - 1

        # Find insertion point
        while l <= r:
            mid = (l + r) // 2

            if arr[mid] < x:
                l = mid + 1
                idx = l
            else:
                r = mid - 1

        # Start with arr[idx]
        res = []
        l = idx - 1
        r = idx

        while len(res) < k:
            if l < 0:
                res.append(arr[r])
                r += 1
            elif r >= len(arr):
                res.append(arr[l])
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1

        return sorted(res)