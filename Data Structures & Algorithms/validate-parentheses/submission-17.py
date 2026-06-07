class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(': ')', '[' : ']', '{' : '}'}


        res = []

        for x in s:
            if x in dic.keys():
                res.append(x)
            else:
                if res and x == dic[res[-1]]:
                    res.pop()
                else:
                    return False

        if len(res) == 0:
            return True
        return False


        