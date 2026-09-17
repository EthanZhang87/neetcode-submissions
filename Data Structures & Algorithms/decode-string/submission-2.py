class Solution:
    def decodeString(self, s: str) -> str:
        res = ''
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                curr = ''
                num = ''
                while stack and stack[-1] != '[':
                    curr = stack.pop() + curr

                stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(int(num) * curr)

        return ''.join(stack)

        