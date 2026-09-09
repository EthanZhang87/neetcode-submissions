class Solution:
    def simplifyPath(self, path: str) -> str:
        res = path.split("/")
        stack = []


        for x in res:
            if x == '' or x == '.':
                continue

            elif x == '..':
                if stack:
                    stack.pop()

            else:
                stack.append(x)
            
        res = '/'

        for x in range(len(stack) - 1):
            res += stack[x] + '/'
        if stack:
            res += stack[-1]

        return res

        
        