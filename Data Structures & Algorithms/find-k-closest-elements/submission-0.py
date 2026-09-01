class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = 0
        res = []

        for i in range(len(arr)):
            if arr[i] < x:
                idx = i + 1
        

        l, r = idx - 1, idx

        while len(res) < k:
            if l < 0:
                res.append(arr[r])
                r += 1

            elif r >= len(arr):
                res.append(arr[l])
                l -= 1

            elif abs(x - arr[l]) == abs(x - arr[r]):
                res.append(arr[l])
                l -= 1

            elif abs(x - arr[l]) < abs(x - arr[r]):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1

        res.sort()
        return res

        


        

        
        