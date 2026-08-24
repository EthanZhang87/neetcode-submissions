class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(numCourses)}
        classesNeeded = [0] * numCourses
        res = []

        for x,y in prerequisites:
            adjList[y].append(x)
            classesNeeded[x] += 1

        queue = deque()

        for x in adjList:
            if classesNeeded[x] == 0:
                queue.append(x)
            

        
        while queue:
            ele = queue.popleft()
            res.append(ele)

            for i in adjList[ele]:
                classesNeeded[i] -= 1
                if classesNeeded[i] == 0:
                    queue.append(i)

        if len(res) != numCourses:
            return []

        return res
                    


        

       

                