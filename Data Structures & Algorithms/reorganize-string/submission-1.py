class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        counts = Counter(s)
        res = ''
        prev = None
        prevCount = 0

        for k, v in counts.items():
            heapq.heappush(heap, (-1 * v, k))

        while heap:
            if not prev:
                ele = heapq.heappop(heap)
                res += ele[1]
                if len(res) == len(s):
                    return res
                prev = ele[1]
                prevCount = ele[0] + 1

            else:
                ele = heapq.heappop(heap)
                if prev == ele[1]:
                    return ''
                res += ele[1]
                if len(res) == len(s):
                    return res
                if prevCount < 0:
                    heapq.heappush(heap, (prevCount, prev))
                prev = ele[1]
                prevCount = ele[0] + 1
        

        return res if len(res) == len(s) else '' 

            
        