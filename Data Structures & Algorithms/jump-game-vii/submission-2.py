class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0

        while q:
            ele = q.popleft()
            start = max(ele + minJump, farthest + 1)
            for j in range(start, min(ele + maxJump + 1, len(s))):
                if s[j] == '0':
                    q.append(j)
                    if j == len(s) - 1:
                        return True

            farthest = ele + maxJump

        return False

                



        