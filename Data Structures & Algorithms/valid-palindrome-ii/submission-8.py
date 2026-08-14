class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check(l, r):
            while l <= r:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1

            return True
        

        l, r = 0, len(s) - 1

        while l <= r:
            if not s[l].isalnum():
                l += 1
            if not s[r].isalnum():
                r -= 1

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1

            else:
                return check(l + 1, r) or check(l, r - 1)

        return True
        
        