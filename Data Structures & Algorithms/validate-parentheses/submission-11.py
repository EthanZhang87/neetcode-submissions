class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{':'}', '[':']', '(':')'}
        arr = []

        for x in s:
            if x in dic.keys():
                arr.append(x)
            elif len(arr) != 0 and dic[arr[-1]] == x:
                arr.pop()
            else:
                return False

        if len(arr) == 0:
            return True
            
        return False




        