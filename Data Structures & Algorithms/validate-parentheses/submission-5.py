class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{':'}', '[':']', '(':')'}
        arr = []
        for x in s:
            if x in dic:
                arr.append(x)
            else:
                if not arr:
                    return False
                elif dic[arr[-1]] == x:
                    arr.pop()
                else:
                    return False

        return len(arr) == 0




        