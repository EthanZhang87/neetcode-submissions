class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = {'a': a, 'b': b, 'c': c}
        heap = []
        res = ''
        for k, v in counts.items():
            if v > 0:
                heapq.heappush(heap, (-1 * v, k))

        prevVal, prevCount = None, 0
        tempVal, tempCount = None, 0
        while heap: 
            if heap[0][1] == prevVal and prevCount == 2:
                ele = heapq.heappop(heap)
                tempVal = ele[1]
                tempCount = ele[0]

                if not heap:
                    break



            if heap[0][1] == prevVal:
                ele2 = heapq.heappop(heap)
                res += ele2[1]
                prevCount += 1
                if ele2[0] + 1 < 0:
                    heapq.heappush(heap, (ele2[0] + 1, ele2[1]))
            else:
                ele2 = heapq.heappop(heap)
                res += ele2[1]

                prevVal = ele2[1]
                prevCount = 1
                if ele2[0] + 1 < 0:
                    heapq.heappush(heap, (ele2[0] + 1, ele2[1]))

            if tempVal:
                heapq.heappush(heap, (tempCount, tempVal))
                tempVal = None
                tempCount = 0

        return res



        

        


        