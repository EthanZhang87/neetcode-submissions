class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegrees = [0] * numCourses
        res = []
        adjList = {}
        for x in prerequisites:
            if x[1] not in adjList:
                adjList[x[1]] = []
            adjList[x[1]].append(x[0])
            inDegrees[x[0]] += 1

        queue = deque()

        for x in range(len(inDegrees)):
            if inDegrees[x] == 0:
                queue.append(x)

        

        while queue: 
            element = queue.popleft()

            res.append(element)
            for i in adjList.get(element, []):
                inDegrees[i] -= 1
                if inDegrees[i] == 0:
                    queue.append(i)
            if len(res) == numCourses:
                return res

        return []

                    


        

       

                