class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for x in range(numCourses)]
        courseCount = 0 
        inDegree = [0] * numCourses

        for x in prerequisites:
            adjList[x[1]].append(x[0])
            inDegree[x[0]] += 1

        queue = deque()

        for x in range(numCourses):
            if inDegree[x] == 0:
                queue.append(x)

        while queue:
            element = queue.popleft()
            courseCount += 1

            for x in adjList[element]:
                inDegree[x] -= 1
                if inDegree[x] == 0:
                    queue.append(x)

        return courseCount == numCourses





                



    





        


            






        
      

        