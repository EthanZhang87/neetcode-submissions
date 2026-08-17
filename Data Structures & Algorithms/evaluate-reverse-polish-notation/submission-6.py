class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []

        operations = ['+', '-', '*', '/']

        newEle = 0
        for x in tokens:
            if x not in operations:
                stack.append(x)

            else:
                ele1 = stack.pop()
                ele2 = stack.pop()
                if x == '+':
                    newEle = int(ele1) + int(ele2)
                elif x == '-':
                    newEle = int(ele2) - int(ele1)
                elif x == '*':
                    newEle = int(ele1) * int(ele2)
                elif x == '/':
                    newEle = int(int(ele2) / int(ele1))

                stack.append(newEle)

        return newEle