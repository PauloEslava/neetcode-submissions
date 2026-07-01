class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        sDict = {}
        tDict = {}

        if len(s) != len(t):
            return False

        for letter in s:
            if letter not in sDict:
                sDict[letter] = 1
            else:
                sDict[letter] += 1

        for letter in t:
            if letter not in tDict:
                tDict[letter] = 1
            else:
                tDict[letter] += 1

        for key in sDict:
            if key not in tDict or sDict[key] != tDict[key]:
                return False

        return True
        
