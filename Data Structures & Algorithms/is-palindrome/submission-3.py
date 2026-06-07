class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        newS = ''.join(x for x in s if x.isalnum())


        return newS.lower()[::-1] == newS.lower()