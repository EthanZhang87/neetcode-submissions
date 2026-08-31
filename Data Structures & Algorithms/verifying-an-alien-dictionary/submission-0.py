class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {}

        for i, char in enumerate(order):
            orderMap[char] = i

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            for i in range(len(w1)):
                if i == len(w2):
                    return False

                if orderMap[w1[i]] < orderMap[w2[i]]:
                    break
                if orderMap[w2[i]] < orderMap[w1[i]]:
                    return False

        return True

        