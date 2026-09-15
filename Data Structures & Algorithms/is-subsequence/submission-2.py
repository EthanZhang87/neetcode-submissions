class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        if not t:
            return False
        curr = 0 

        for x in t:
            if x == s[curr]:
                curr += 1
                if curr == len(s):
                    return True
        return curr == len(s)
        