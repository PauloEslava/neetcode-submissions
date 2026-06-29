class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        s = s.replace("?", "")
        s = s.replace("!", "")
        s = s.replace(".", "")
        s = s.replace(",", "")
        s = s.replace("'", "")
        s = s.replace(":", "")
        s = s.replace(";", "")

        reverse = s[::-1]

        if reverse == s:
            return True

        return False
        