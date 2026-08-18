class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        check = []
        for i in s:
            if i.isalnum():
                check.append(i)
        return check == check[::-1]
        