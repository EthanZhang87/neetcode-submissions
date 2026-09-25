class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = [False] * len(queries)
        adjList = {}
        for schedule in prerequisites:
            if schedule[0] not in adjList:
                adjList[schedule[0]] = []

            adjList[schedule[0]].append(schedule[1])

        for x in range(len(queries)):
            visited = {queries[x][0]}
            queue = deque([queries[x][0]])

            while queue:
              
                element = queue.popleft()
                for course in adjList.get(element, []):
                    if course == queries[x][1]:
                        res[x] = True
                        break
                    else:
                        if course not in visited:
                            visited.add(course)
                            queue.append(course)

        return res


        

        