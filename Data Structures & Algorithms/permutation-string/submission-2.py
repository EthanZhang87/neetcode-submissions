class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}

        for x in s1:
            count[x] = count.get(x, 0) + 1

        l = 0

        curr = {}
        have, need = 0, len(count)


        for x in range(len(s1) - 1):
            curr[s2[x]] = curr.get(s2[x], 0) + 1
            if s2[x] in s1 and curr[s2[x]] == count[s2[x]]:
                have += 1

        for r in range(len(s1) - 1, len(s2)):
            
            curr[s2[r]] = curr.get(s2[r], 0) + 1
            if s2[r] in s1 and curr[s2[r]] == count[s2[r]]:
                have += 1
                
            if have == need and len(curr) == len(count):
                    return True
            wasTrue = False
            if s2[l] in s1 and curr[s2[l]] == count[s2[l]]:
                wasTrue = True
            curr[s2[l]] -= 1
            if s2[l] in s1 and wasTrue and curr[s2[l]] != count[s2[l]]:
                have -= 1

            if curr[s2[l]] == 0:
                curr.pop(s2[l])
            
            l += 1

        return False

            

                