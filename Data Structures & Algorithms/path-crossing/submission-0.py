class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()

        curr = [0, 0]
        visited.add((0,0))

        for x in path:
            if x == 'N':
                curr[1] += 1
                if (curr[0], curr[1]) in visited:
                    return True

                visited.add((curr[0], curr[1]))
            if x == 'S':
                curr[1] -= 1
                if (curr[0], curr[1]) in visited:
                    return True

                visited.add((curr[0], curr[1]))

            if x == 'E':
                curr[0] += 1
                if (curr[0], curr[1]) in visited:
                    return True

                visited.add((curr[0], curr[1]))

            if x == 'W':
                curr[0] -= 1
                if (curr[0], curr[1]) in visited:
                    return True

                visited.add((curr[0], curr[1]))

        return False

            
        