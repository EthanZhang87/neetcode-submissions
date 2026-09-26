class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        time = 0
        heap = []
        avaliableHeap = []

        for x in range(len(tasks)):
            heapq.heappush(heap, (tasks[x][0], tasks[x][1], x))

        while heap or avaliableHeap:
            if not avaliableHeap and heap and time < heap[0][0]:
                time = heap[0][0]
                
            while heap and heap[0][0] <= time:
                ele = heapq.heappop(heap)
                heapq.heappush(avaliableHeap, (ele[1], ele[2]))
                
                

            if avaliableHeap:
                element = heapq.heappop(avaliableHeap)
                res.append(element[1])
                time += element[0]






        
            

        return res

        