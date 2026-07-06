class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1chars = [0] * 26
        s2chars = [0] * 26
        left = 0
        k = len(s1)

        for char in s1:
            charPos = ord(char) - ord('a')
            s1chars[charPos] += 1 

        for right in range(left, len(s2)):
            if right - left >= k:
                charPos = ord(s2[left]) - ord('a')
                s2chars[charPos] -= 1
                left += 1
            charPos = ord(s2[right]) - ord('a')
            s2chars[charPos] += 1
            right += 1
            if s2chars == s1chars:
                return True

        return False