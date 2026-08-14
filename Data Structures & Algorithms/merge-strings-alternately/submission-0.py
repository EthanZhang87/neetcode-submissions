class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        start1, start2 = 0, 0

        while start1 < len(word1) and start2 < len(word2):
            res += word1[start1]
            res += word2[start2]
            start1 += 1

            start2 += 1

        if start1 < len(word1):
            res += word1[start1:]

        if start2 < len(word2):
            res += word2[start2:]

        return res

        