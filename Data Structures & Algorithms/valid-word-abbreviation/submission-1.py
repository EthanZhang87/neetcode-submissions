class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l1, l2 = 0, 0

        while l1 < len(word) and l2 < len(abbr):
            if word[l1] == abbr[l2]:
                l1 += 1
                l2 += 1
            else:
                if not abbr[l2].isdigit() or abbr[l2] == '0':
                    return False
                count = ''
                while l2 < len(abbr) and abbr[l2].isdigit():
                    count += abbr[l2]
                    l2 += 1

                l1 += int(count)

        return l1 == len(word) and l2 == len(abbr)
        