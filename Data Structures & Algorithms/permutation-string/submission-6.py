class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1chars = [0] * 26
        s2chars = [0] * 26
        k = len(s1)
        left = 0
        
        for char in s1:
            charPos = ord(char) - ord('a')
            s1chars[charPos] += 1

        # We basically have to do sliding window so that
        # K = len(s1) and we check in s2 for a window where the characters appear

        for right in range(left, len(s2)):
            if right - left >= k:
                charPos = ord(s2[left]) - ord('a')
                s2chars[charPos] -= 1
                left += 1
            charPos = ord(s2[right]) - ord('a')
            s2chars[charPos] += 1
            if s2chars == s1chars:
                return True
        return False