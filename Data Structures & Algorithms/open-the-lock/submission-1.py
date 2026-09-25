class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        res = 0
        start = ['0', '0', '0', '0']
        visited = set(''.join(start))

        queue = deque([start])

        while queue:
            for x in range(len(queue)):
                element = queue.popleft()
                if ''.join(element) == target:
                    return res

                for i in range(len(element)):
                    newState1 = element.copy()
                    newState2 = element.copy()
                    newEle1 = (int(element[i]) + 1) % 10
                    newEle2 = (int(element[i]) - 1) % 10

                    newState1[i] = str(newEle1)
                    if ''.join(newState1) not in deadends and ''.join(newState1) not in visited:
                        visited.add(''.join(newState1))
                        queue.append(newState1)

                    newState2[i] = str(newEle2)
                    if ''.join(newState2) not in deadends and ''.join(newState2) not in visited:
                        visited.add(''.join(newState2))
                        queue.append(newState2)

            res += 1

        return -1 

                    



        