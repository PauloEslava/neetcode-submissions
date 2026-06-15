class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = []
        t_chars = []
        for char in s:
            s_chars.append(char)
        for char in t:
            t_chars.append(char)
        t_chars.sort()
        s_chars.sort()
        palindromeStatus = (t_chars == s_chars)

        return palindromeStatus
        