class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = [0] * numCourses
        adjList = {}
        for x, y in prerequisites:
            if y not in adjList:
                adjList[y] = []

            adjList[y].append(x)
            in_degrees[x] += 1

        queue = deque()

        for x in range(numCourses):
            if in_degrees[x] == 0:
                queue.append(x)

        while queue:
            element = queue.popleft()

            for x in adjList.get(element, []):
                in_degrees[x] -= 1
                if in_degrees[x] == 0:
                    queue.append(x)

        for x in in_degrees:
            if x != 0:
                return False

        return True


        





                



    





        


            






        
      

        