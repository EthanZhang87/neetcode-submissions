class Solution:
    def isPalindrome(self, s: str) -> bool:


        s = [s[x] for x in range(len(s)) if s[x].isalnum()]
        left, right = 0, len(s) - 1

        while left < right:
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True
        