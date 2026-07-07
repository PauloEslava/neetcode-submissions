class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = [0] * 26
        tChars = [0] * 26

        for char in s:
            charPos = ord(char) - ord('a')
            sChars[charPos] += 1

        for char in t:
            charPos = ord(char) - ord('a')
            tChars[charPos] += 1

        return tChars == sChars
        
        
