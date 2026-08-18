class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCounter = {}
        tCounter = {}
        for i in s:
            sCounter[i] = sCounter.get(i, 0) + 1
        for j in t:
            tCounter[j] = tCounter.get(j, 0) + 1

        return sCounter.items() == tCounter.items()