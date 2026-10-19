class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegrees = [0] * numCourses
        res = []

        adjList = defaultdict(list)
        queue = deque()
        for x in prerequisites:
            adjList[x[1]].append(x[0])
            inDegrees[x[0]] += 1

        for x in range(numCourses):
            if inDegrees[x] == 0:
                queue.append(x)
                res.append(x)
    
        while queue:
            ele = queue.popleft()
            for nei in adjList[ele]:
                inDegrees[nei] -= 1
                if inDegrees[nei] == 0:
                    res.append(nei)
                    queue.append(nei)

        
        if len(res) == numCourses:
            return res
        return []





        

                    


        

       

                