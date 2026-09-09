class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = len(position)
        speed_map = {}

        for x in range(len(position)):
            speed_map[position[x]] = speed[x]

        position.sort()
        stack = []

        for x in range(len(position) - 1, -1, -1):
            time = (target - position[x]) / speed_map[position[x]]

            if not stack or stack[-1] < time:
                stack.append(time)
           

        return len(stack)


      



