class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        stack = []

        for x in operations:
            if x == '+':
                curr = int(stack[-1]) + int(stack[-2])
      
                stack.append(curr)
                


            elif x == 'D':
                curr = 2 * int(stack[-1])
 
                stack.append(curr)

            elif x == 'C':
                stack.pop()

            else:
                stack.append(x)

        for x in stack:
            res += int(x)
        print(stack)
        return res


        