class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        preMap = {x : [] for x in range(numCourses)}

        for x in prerequisites:
            preMap[x[0]].append(x[1])

        def dfs(curr):
            if curr in visited:
                return False

            if preMap[curr] == []:
                return True
            visited.add(curr)
            for x in preMap[curr]:
                if not dfs(x): 
                    return False
                
            visited.remove(curr)
            preMap[curr] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
                



    





        


            






        
      

        