class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        notAlphNum = []
        for char in s:
            if char.isalnum() == False:
                notAlphNum.append(char)

        for char in notAlphNum:
            s = s.replace(char, "")

        reverse = s[::-1]

        if reverse == s:
            return True

        return False
        